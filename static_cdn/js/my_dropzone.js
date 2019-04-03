var accept = ".pdf";
Dropzone.autoDiscover = true;

// Dropzone class:
var myDropzone = new Dropzone("#mydropzone", {
  url: "/file/post",
   acceptedFiles: accept,
   uploadMultiple: false,
   createImageThumbnails: false,
   addRemoveLinks: true,
    maxFiles: 1,
    maxfilesexceeded: function(file) {
        this.removeAllFiles();
        this.addFile(file);
    },init: function() {
    this.on('error', function(file, errorMessage) {
      var mypreview = document.getElementsByClassName('dz-error');
      mypreview = mypreview[mypreview.length - 1];
      mypreview.classList.toggle('dz-error');
      mypreview.classList.toggle('dz-success');
    });
  }
  
  });