var fileTarget = $('#file');
  fileTarget.on('change', function(){
      var cur=$(".filebox input[type='file']").val();
    $(".upload-name").val(cur);
  });

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

const dropArea = document.getElementById("drop-file");

function highlight(e) {
  preventDefaults(e);
  dropArea.classList.add("highlight");
}

function unhighlight(e) {
  preventDefaults(e);
  dropArea.classList.remove("highlight");
}

dropArea.addEventListener("dragenter", highlight, false);
dropArea.addEventListener("dragover", highlight, false);
dropArea.addEventListener("dragleave", unhighlight, false);

function handleDrop(e) {
  unhighlight(e);
  let dt = e.dataTransfer;
  let files = dt.files;

  console.log(files);

  // addToFileList
  // ...
}