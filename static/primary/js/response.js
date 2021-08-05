var copy_btn=document.querySelector('.copy'),
    save_as=document.querySelector('.save_as_txt'),
    share=document.querySelector('.share'),
    font_size=document.querySelector('.font-size'),
    undo=document.querySelector('.undo')  
    get_alert=document.querySelector('.prompt')


// copy to clipboard function

copy_btn.addEventListener('click', set_copy)

function set_copy(){
  var copyTextarea = document.querySelector('.output-data');
  copyTextarea.focus();
  copyTextarea.select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';

    var doodle = document.getElementById("doodle");
    doodle.src = "https://static-file-container.s3.ap-south-1.amazonaws.com/primary/images/copied.svg";

    get_alert.innerText='Data Copied'
    console.log('Copying text command was ' + msg);
  } catch (err) {
    console.log('Oops, unable to copy');
  }

}


// remove alert after 2 seconds
function clear_it(){
  get_alert.remove()
}
setTimeout(clear_it, 4500)


// change 
