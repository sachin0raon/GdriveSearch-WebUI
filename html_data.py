HTML_DATA = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>CyberSpace - FileSearch</title>
  <meta content="Index page" name="description">
  <!-- Favicons -->
  <link href="https://raw.githubusercontent.com/sachinOraon/media-server-suite/master/volumes/home-page/assets/img/favicon.png" rel="icon">
  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,500,500i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">
  <!-- Vendor CSS Files -->
  <link href="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/vendor/animate.css/animate.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/vendor/remixicon/remixicon.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">
  <!-- Template Main CSS File -->
  <link href="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/css/style.css" rel="stylesheet">
</head>
<body>
  <div class="modal fade" id="infoModal" aria-hidden="true">
    <div class="modal-dialog modal-sm">
      <div class="modal-content">
        <div class="modal-header">
          <h4 class="modal-title">Information</h4>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body"></div>
        <div class="modal-footer">
          <button type="button" class="btn btn-outline-danger btn-sm" data-bs-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>
  <!-- ======= Header ======= -->
  <header id="header" class="fixed-top d-flex align-items-center  header-transparent ">
    <div class="container d-flex align-items-center justify-content-between">
      <div class="logo">
        <h1><a href="https://github.com/sachin0raon/GdriveSearch-WebUI" target="_blank">CyberSpace Cloud ☁</a></h1>
      </div>
    </div>
  </header><!-- End Header -->
  <!-- ======= Hero Section ======= -->
  <section id="hero" class="d-flex flex-column justify-content-end align-items-center">
    <div id="heroCarousel" data-bs-interval="5000" class="container carousel carousel-fade" data-bs-ride="carousel">
      <!-- Slide 1 -->
      <div class="carousel-item active">
        <div class="carousel-container">
          <h2 class="animate__animated animate__fadeInDown">GDrive Media Search™</h2>
          <p class="animate__animated fanimate__adeInUp">Welcome to the multimedia search engine, a service created to search and download files stored in GDrives. You can also use the Telegram <strong><a href="https://github.com/sachin0raon/GdriveSearchBot">bot</a></strong> to search files. Please join our Telegram <strong><a href="https://t.me/+xAIvM07WT1s4MWI1">group</a></strong> for more details.</p><div><input type="text" class="form-control" name="searchQueryBox" placeholder="Enter search query"></div><a href="#" class="btn-get-started animate__animated animate__fadeInUp font-weight-bold" id="searchBtn">Search</a>
        </div>
      </div>
    </div>
    <svg class="hero-waves" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 24 150 28 " preserveAspectRatio="none">
      <defs>
        <path id="wave-path" d="M-160 44c30 0 58-18 88-18s 58 18 88 18 58-18 88-18 58 18 88 18 v44h-352z">
      </defs>
      <g class="wave1">
        <use xlink:href="#wave-path" x="50" y="3" fill="rgba(255,255,255, .1)">
      </g>
      <g class="wave2">
        <use xlink:href="#wave-path" x="50" y="0" fill="rgba(255,255,255, .2)">
      </g>
      <g class="wave3">
        <use xlink:href="#wave-path" x="50" y="9" fill="#fff">
      </g>
    </svg>
  </section><!-- End Hero -->
  <main id="main">
    <!-- ======= Services Section ======= -->
    <section id="results" class="services">
      <div class="container">
        <div class="section-title" data-aos="zoom-out">
          <h2 id="searchCount" style="font-size: 20px;"></h2>
          <p id="searchQuery"></p>
        </div>
        <div id="searchResults" class="row"></div>
      </div>
    </section><!-- End Services Section -->
  </main><!-- End #main -->
  <!-- ======= Footer ======= -->
  <footer id="footer">
    <div class="container">
      <h3>GDrive File Search</h3>
      <p>Search and download the files stored in multiple shared drives.</p>
      <div class="social-links">
        <a href="https://github.com/sachin0raon/GdriveSearch-WebUI" target="_blank"><i class="bx bxl-github"></i></a>
        <a href="https://t.me/+xAIvM07WT1s4MWI1" target="_blank"><i class="bx bxl-telegram"></i></a>
        <a href="https://t.me/+xAIvM07WT1s4MWI1" target="_blank"><i class='bx bx-cloud-download'></i></a>
      </div>
      <div class="copyright">
        &copy; Copyright <strong><span>CyberSpace™</span></strong>. All Rights Reserved
      </div>
      <div class="credits">
        Designed by <a href="https://bootstrapmade.com/">BootstrapMade</a>
      </div>
    </div>
  </footer><!-- End Footer -->
  <a href="#results" class="back-to-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>
  <!-- Vendor JS Files -->
  <script src="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/vendor/aos/aos.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/vendor/swiper/swiper-bundle.min.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/sachinOraon/Torrent-Leecher@master/js/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js" crossorigin="anonymous"></script>
  <!-- Template Main JS File -->
  <script src="https://cdn.jsdelivr.net/gh/sachinOraon/media-server-suite@master/volumes/home-page/assets/js/main.js"></script>
  <script>
    $(document).ready(function(){
      $('#results, #footer').hide();
      var queryInput = $('input[name="searchQueryBox"]');
      var initialTxt = queryInput.val().trim();
      // provide the URL of your flask server
      var apiUrl = window.location.protocol+'//'+window.location.host;
      var isPopoverActive = false;
      queryInput.popover({
        title    : '<span id="popoverHead">Suggestions</span>',
        content  : '<div id="titlesBody"><div>Loading <div class="spinner-grow spinner-grow-sm text-warning" role="status"><span class="visually-hidden"></span></div></div></div>',
        html     : true,
        placement: 'auto',
        trigger  : 'manual',
        boundary : 'window',
        delay    : {show: 0, hide: 300}
      });
      $("#searchBtn").on('click', function() {
        var query = queryInput.val().replace(/[^A-Za-z0-9-_. ]/g, "").trim();
        if (query === "") {
          queryInput.popover('show');
          $('#popoverHead').html('Info');
          $('#titlesBody').html('<strong>Please enter something to search !</strong>');
          setTimeout(() => { queryInput.popover('hide');}, 1000);
        } else {
          initialTxt = query;
          queryInput.popover('hide');
          $('#searchResults').html('');
          $('#results, #footer').hide();
          $('#searchBtn').html('Searching <div class="spinner-grow spinner-grow-sm text-warning" role="status"><span class="visually-hidden">Loading...</span></div>');
          $.ajax({
            url: apiUrl+'/search/'+encodeURIComponent(query),
            method: 'GET',
            dataType: 'json',
            crossOrigin: true,
            crossDomain: true,
            headers: {'Access-Control-Allow-Origin': '*',},
            success: function(response) {
              if (response.status == "success") {
                let filesCount = Object.keys(response).length-1;
                if (filesCount > 0) {
                  $('#searchQuery').text(query);
                  $('#searchCount').html('Files Found: <strong>'+filesCount+'</strong>');
                  let htmlData = '';
                  for (let fileId in response) {
                    if (fileId == "status") {
                      continue;
                    }
                    let fileName = response[fileId].name;
                    let fileSize = response[fileId].size;
                    let fileMimeType = response[fileId].mimeType;
                    let endPoint = encodeURIComponent(fileName)+'?id='+fileId;
                    let dlLink1 = 'DL_WORKER_1/'+endPoint;
                    let dlLink2 = 'DL_WORKER_2/'+endPoint;
                    let gdriveLink = 'https://drive.google.com/uc?id='+fileId+'&export=download';
                    let colorHex = '#'+Math.floor(Math.random()*16777215).toString(16);
                    htmlData += '<div class="col-lg-6 col-md-6 mt-3"><div class="icon-box" data-aos="zoom-in-left"><div class="icon"><i class="bx bxs-videos" style="color: '+colorHex+';"></i></div><h4 class="title text-break fs-6"><a href="'+gdriveLink+'" target="_blank" referrerpolicy="same-origin">📂 '+fileName+'</a></h4><p class="description fw-bold">💾 '+fileSize+'</p><p class="description mt-1"><a class="btn btn-outline-primary btn-sm" role="button" href="'+dlLink1+'">⚡<strong> Download 1</strong></a>&nbsp;&nbsp;<a class="btn btn-outline-success btn-sm" role="button" href="'+dlLink2+'">⚡<strong> Download 2</strong></a></p>';
                    if (fileMimeType.search('video') >= 0) {
                      let mediaLink = 'DL_WORKER_3/'+endPoint;
                      let vlcLink = 'vlc://'+mediaLink;
                      let mxpLink = 'intent:'+mediaLink+'#Intent;package=com.mxtech.videoplayer.ad;S.title='+fileName+';end';
                      let npLink = 'nplayer-'+mediaLink;
                      htmlData += '<p class="description mt-1"><a href="'+vlcLink+'" style="color: #444444;">▶️<strong> VLC</strong></a>&nbsp;&nbsp;<a href="'+mxpLink+'" style="color: #444444;">▶️<strong> MX Player</strong></a>&nbsp;&nbsp;<a href="'+npLink+'" style="color: #444444;">▶️<strong> nPlayer</strong></a></p>';
                    }
                    htmlData += '</div></div>';
                  }
                  $('#searchResults').html(htmlData);
                  $('#searchBtn').html('Search');
                  $('#results, #footer').show();
                  $("html, body").animate({ scrollTop: $('#results').offset().top }, 500);
                } else {
                  $('#infoModal div.modal-body').html('<p class="h6">Unable to find any files for the query: <u><em><b>'+query+'</b></em></u>. Please refine your search criteria and retry ❗</p>');
                  $('#searchBtn').html('Search');
                  $('#infoModal').modal('show');
                }
              } else {
                $('#infoModal div.modal-body').html('<p class="h6">Error occurred while searching: <u><em><b>'+query+'<b></em>.</u> Reason: <strong>'+response.msg+'</strong> Please retry ❗');
                $('#infoModal').modal('show');
                $('#searchBtn').html('Search');
              }
            },
            error: function(xhr, status, error) {
              var errorMessage = 'Failed to send request to server: '+xhr.statusText+'['+xhr.status+']';
              window.alert('Internal Server Error - '+errorMessage+' Please retry again.');
              $('#searchBtn').html('Search');
            }
          });
        }
      });
      $("#hero").on('click', function(){ if(isPopoverActive) { queryInput.popover('hide'); isPopoverActive=false; } });
      function fetchTitles(queryParam) {
        if (queryParam == queryInput.val().trim()) {
          $.ajax({
            url: apiUrl+'/titles/'+encodeURIComponent(queryParam),
            method: 'GET',
            dataType: 'json',
            crossOrigin: true,
            crossDomain: true,
            success: function(response){
              if (response.status == "success"){
                if (response.titles.length < 1){
                  $("#titlesBody").html('<span><i class="bx bx-error-circle"></i>&nbsp;<strong>Nothing found !</strong></span>');
                } else {
                  let titlesData = '';
                  for (let i in response.titles) {titlesData += '<div style="cursor:pointer;"><i class="bx bx-search-alt-2"></i> '+response.titles[i]+'</div>';}
                  $("#titlesBody").html(titlesData);
                  $("#titlesBody div").on('click', function(){
                    var inputTxt = $(this).text().trim();
                    queryInput.val(inputTxt);
                    initialTxt = inputTxt;
                    queryInput.popover('hide');
                    isPopoverActive=false;
                    $("#searchBtn").click();
                  });
                  $("#titlesBody div").hover(
                    function(){ $(this).addClass("mark"); $(this).html('<i class="bx bx-search-alt-2"></i> <strong>'+$(this).text()+'</strong>'); },
                    function(){ $(this).removeClass("mark"); $(this).html('<i class="bx bx-search-alt-2"></i> '+$(this).text().trim()); }
                  );
                }
              } else { $("#titlesBody").html('<span><i class="bx bx-error"></i>&nbsp;<strong>Failed to load, please retry !</strong></span>'); }
            },
            error: function(xhr, status, error) {
              $("#titlesBody").html('<span><i class="bx bx-error"></i>&nbsp;<strong>Internal Server Error, please retry !</strong></span>');
            }
          });
          if (isPopoverActive) {
            $("#titlesBody").html('<div>Loading <div class="spinner-grow spinner-grow-sm text-warning" role="status"><span class="visually-hidden"></span></div></div>');
          } else {
            queryInput.popover('show');
            isPopoverActive = true;
          }
        }
      }
      queryInput.keyup(function(event) {
        var keycode = event.which;
        if (keycode == 13) $("#searchBtn").click();
        else {
          var inpTxt = queryInput.val().trim();
          if(inpTxt.length < 2) if (isPopoverActive) { queryInput.popover('hide'); isPopoverActive=false; }
          if (inpTxt != initialTxt && keycode != 8) {
            initialTxt = inpTxt;
            if (inpTxt.length >= 2) setTimeout(fetchTitles, 1100, inpTxt);
          }
        }
        event.stopPropagation();
      });
      $('#infoModal').on('hidden.bs.modal', function() { $('#infoModal div.modal-body').html(''); });
      queryInput.on('hidden.bs.popover', function(){
        $("#titlesBody").html('<div>Loading <div class="spinner-grow spinner-grow-sm text-warning" role="status"><span class="visually-hidden"></span></div></div>');
      });
    });
  </script>
</body>
</html>
'''
