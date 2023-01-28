import os
import re
import io
import pickle
import logging
import humanize
import requests
import json
import asyncio
from flask import Flask
from flask_cors import CORS
from urllib.parse import unquote
from dotenv import load_dotenv
from imdb import Cinemagoer
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from html_data import HTML_DATA

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
CONFIG_FILE_URL = os.getenv("CONFIG_FILE_URL")
DLWORKER_LIST = list()
PICKLE_FILE_NAME = "token.pickle"
MAX_RESULTS = 30
REMOVE_DUPLICATES = False
QUALITIES = ["360", "480", "720", "1080", "1440", "2160"]
HTML_PAGE = HTML_DATA

flask_app = Flask(__name__)
CORS(flask_app)

def setup_config() -> bool:
    global HTML_PAGE
    global DLWORKER_LIST
    global MAX_RESULTS
    global REMOVE_DUPLICATES
    if CONFIG_FILE_URL is not None:
        logger.info("Downloading config file")
        try:
            config_file = requests.get(url=CONFIG_FILE_URL)
            if config_file.ok:
                with open('config.env', 'wt', encoding='utf-8') as f:
                    f.write(config_file.text)
                logger.info("Loading config values")
                if load_dotenv('config.env', override=True):
                    pickle_file = requests.get(url=os.environ['PICKLE_FILE_URL'])
                    if pickle_file.ok:
                        with open(PICKLE_FILE_NAME, 'wb') as f:
                            f.write(pickle_file.content)
                        MAX_RESULTS = int(os.environ['MAX_RESULTS'])
                        REMOVE_DUPLICATES = os.environ['REMOVE_DUPLICATES'].lower() == "true"
                        DLWORKER_LIST = json.loads(os.environ['DLWORKER_LIST'])
                        if len(DLWORKER_LIST) != 3:
                            logger.error("Provide 3 download worker URL")
                        else:
                            for index, url in enumerate(DLWORKER_LIST):
                                HTML_PAGE = HTML_PAGE.replace(f'DL_WORKER_{index + 1}', url)
                            logger.info("Config setup completed")
                            return True
                    else:
                        logger.error(f"Failed to download {PICKLE_FILE_NAME}")
            else:
                logger.error("Error while downloading config file")
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, IndexError, KeyError, json.JSONDecodeError) as err:
            logger.error(f"Failed to setup config: {str(err)}")
    else:
        logger.error("CONFIG_FILE_URL is None")
    return False

if setup_config() is False:
    logger.error("Error setting up config")

def isDownloadable(fileId, creds, shared_list) -> None:
    try:
        gdrive = build('drive', 'v3', credentials=creds, cache_discovery=False)
        req = gdrive.files().get_media(fileId=fileId)
        buf = io.BytesIO()
        MediaIoBaseDownload(buf, req, chunksize=1024*1024*2).next_chunk()
        buf.close()
        gdrive.close()
    except Exception:
        shared_list.append(fileId)

async def filter_files(fileId, creds, shared_list):
    await asyncio.to_thread(isDownloadable, fileId, creds, shared_list)

async def check_download(creds, files) -> None:
    shared_list = list()
    await asyncio.gather(*[asyncio.create_task(filter_files(fileId, creds, shared_list)) for fileId in files])
    for fileId in shared_list:
        files.pop(fileId)
    del shared_list

def contains(substr: list, fullstr: str) -> bool:
    for s in substr:
        if fullstr.find(s.lower()) == -1:
            return False
    return True

def get_oauth_creds():
    logger.info("Loading token.pickle file")
    with open(PICKLE_FILE_NAME, 'rb') as f:
        credentials = pickle.load(f)
        if credentials and credentials.expired and credentials.refresh_token:
            try:
                credentials.refresh(Request())
            except RefreshError:
                logger.error("Failed to refresh token")
                return None
        return credentials

@flask_app.get('/')
def home() -> str:
    return HTML_PAGE

@flask_app.get("/search/<query>")
def search(query: str) -> dict:
    query = unquote(query)
    query = re.sub('[^a-zA-Z0-9-_. ]', '', query)
    logger.info(f"Searching: {query}")
    quality = None
    for res in QUALITIES:
        if re.search(res, query):
            quality = res
            break
    count = 0
    files_md5 = set()
    response_data = dict()
    try:
        creds = get_oauth_creds()
        service = build('drive', 'v3', credentials=creds, cache_discovery=False)
        gdrive_query = "mimeType != 'application/vnd.google-apps.folder' and "
        query_list = re.split(" ", query)
        for text in query_list:
            if quality is not None and re.search(quality, text):
                continue
            gdrive_query += f"name contains '{text}' and "
        gdrive_query += "trashed=false"
        results = service.files().list(supportsAllDrives=True, includeItemsFromAllDrives=True,
                                       q=gdrive_query, corpora='allDrives', spaces='drive',
                                       fields='files(id, name, mimeType, size, md5Checksum)').execute()["files"]
        service.close()
        for file in results:
            md5 = file.get('md5Checksum')
            if count >= MAX_RESULTS:
                break
            elif REMOVE_DUPLICATES is False and md5 in files_md5:
                continue
            else:
                files_md5.add(md5)
            if file.get('mimeType') == 'application/vnd.google-apps.shortcut' or contains(query_list, file.get('name').lower()) is False:
                continue
            response_data[file.get('id')] = {'name': file.get('name'), 'size': f"{humanize.naturalsize(file.get('size', 0))}", 'mimeType': file.get('mimeType')}
            count += 1
        asyncio.run(check_download(creds, response_data))
        logger.info(f"Query: {query}, Found: {len(response_data)}")
        response_data['status'] = 'success'
        return response_data
    except Exception as err:
        logger.error(f"Failed to search:{query} error: {str(err)}")
        return {'status': 'error', 'msg': f'Internal Server Error[{str(err)}]'}

@flask_app.get("/titles/<query>")
def titles(query: str) -> dict:
    results = dict()
    title = []
    try:
        ia = Cinemagoer()
        query = unquote(query)
        logger.info(f"Fetching titles for: {query}")
        for movie in ia.search_movie(title=query, results=10):
            name = movie.data.get('title').strip()
            year = movie.data.get('year')
            kind = movie.data.get('kind')
            if year is not None and kind == 'movie':
                name += f" {str(year)}"
            title.append(name)
        results['titles'] = title
        results['status'] = 'success'
    except Exception:
        results['status'] = 'error'
    return results
