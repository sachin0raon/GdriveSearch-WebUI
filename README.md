# GDriveSearch-WebUI
Hello there, 🌐 I am a simple web interface that's  designed to fetch files from Google Drive and serve the seeker.

### First of all, create three copies [Cloudflare Workers](https://workers.cloudflare.com/)
📄 [Worker Source Code](https://github.com/sachin0raon/GdriveSearchBot/blob/main/cloudflare_worker.js). These workers will be used to download files. Make sure to fill in these details.
```sh
const authConfig = {
  "client_id": "",
  "client_secret": "",
  "refresh_token": ""
};
```

### Prepare config.env file
Create an env file in [Github Gist](https://gist.github.com/) or any other place but make sure to provide the direct download link of that file.
```sh
PICKLE_FILE_URL = ""
DLWORKER_LIST = '["https://ABC.workers.dev", "https://DEF.workers.dev", "https://GHI.workers.dev"]'
MAX_RESULTS = 30
REMOVE_DUPLICATES = False
```

### Build and run the docker image
```sh
docker build -t gdrive-search:latest .

docker run -d \
  --name=GDriveSearch-WebUI \
  -e CONFIG_FILE_URL="github gist link of config.env" \
  -p 8080:8080 \
  --restart=unless-stopped \
  gdrive-search:latest gunicorn --bind 0.0.0.0:8080 main:flask_app
```
#### Finally, navigate to [http://127.0.0.1:8080](http://127.0.0.1:8080)
