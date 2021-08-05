$(document).ready(function(){
  $('input[type="file"]').change(function(e){
      var fileName = e.target.files[0];
      // show prompt with selected file name when user select file.
      console.log(document.querySelector("#id_photo").nextSibling.nextSibling.innerText=`Selected file => ${fileName.name}`)

       // hide prompt when reset event happen
      var get_reset=document.querySelector('.reset').addEventListener('click', next_action)
      function next_action(z){
        console.log(document.querySelector("#id_photo").nextSibling.nextSibling.innerText=`Please Select Image`)
      }

  });

});
// overlay
overlay=document.querySelector('.overlay')
// preloader
preloader=document.querySelector('.preloader')
// document.querySelector('.loader')
form=document.querySelector('#upload-form')
form.addEventListener('submit', get_loader)

function get_loader(){
  // show loader
  overlay.style.display='block'; 
  preloader.style.display='block'
}

