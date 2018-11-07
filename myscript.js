/*
Event types for EventListener:
mouse events - mousedown, mouseup, click, dblclick, mouseover
touch events - touchstart, touchend
keyboard events - keydown, keyup, keypress
form events - focus, change, submit
window events - scroll, resize
*/
var output_element = function(){
  console.log(this);
}
var header = document.getElementById('my_header');
header.addEventListener('click', output_element);
/*basically when someone clicks we run the output_element
  function which just console.logs this.;

  */
  var change_class = function(){
    if (this.className ==="red") {
      this.className = "green";
    } else if (this.className === "green") {
      this.className = "red";
    }
  }
  var div = document.getElementById("main_box");
div.addEventListener('mouseover', change_class);
