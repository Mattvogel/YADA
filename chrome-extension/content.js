(function() {
    var time = 20000; // time before we close the popup again.
    [].forEach.call(
        document.querySelectorAll('.page-content .yj-tabular-data-name'),
        function(el){

          var fileid = el.href.match(/\/(\d+)$/)[1];
          var downloadPath = "https://www.yammer.com/api/v1/uploaded_files/"+fileid+"/download";
          var popup = window.open(downloadPath);

          // Close timout. You can skip this and just close all browser windows if you want.
          setTimeout(function (argument) {
              popup.close();
          }, time)

        }
      );
})();
