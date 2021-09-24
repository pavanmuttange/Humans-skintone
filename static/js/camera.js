(function() {
    Webcam.set({
        width: 220,
        height: 190,
        image_format: 'jpeg',
        jpeg_quality: 100
    });
    Webcam.attach('#camera');
  
    // SHOW THE SNAPSHOT.
    takeSnapShot = function () {
            Webcam.snap(function (data_uri) {
            document.getElementById('snap').innerHTML = '<img src="' + data_uri +' " width="150px" height="150px" />';
            document.getElementById('snapShot').value = data_uri ;
            document.getElementById('snap123').hidden =  true  ;
                // document.write(data_uri);
        });
    }
})();