var nav = document.getElementById('main_nav');
console.log(nav);

var centred = document.getElementsByClassName("centre");
for (var i = 0; i < centred.length; i++) {
  console.log(centred[i]);
}
var p = document.getElementsByTagName('p');
for (var i = 0; i < p.length; i++) {
  console.log(p[i]);
}
/*
SAME AS ABOVE JUST SELECTS SPECIFIC CSS SELECTORS
var p = document.querySelectorAll('p');
for (var i = 0; i < p.length; i++) {
  console.log(p[i]);
}
SAME AS VERY FIRST JUST SELECTS CERTAIN ELEMENT
var nav = document.querySelector('#main_nav');
console.log(nav);
*/
var paragraphs = document.getElementsByTagName('p');
for (var i = 0; i < paragraphs.length; i++) {
  paragraphs[i].className = "right";
}
/*How to print the inside of an element (innerHTML)*/
var paragraph = document.getElementsByTagName('p');
for (var i = 0; i < paragraph.length; i++) {
  console.log(paragraph[i].innerHTML);
}
var body = document.getElementsByTagName('body') [0];
body.innerHTML = "<h1> IT DISAPPEARED! </h1>"
