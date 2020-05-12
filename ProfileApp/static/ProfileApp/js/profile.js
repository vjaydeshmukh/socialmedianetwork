
            
/*

Full-page view:

https://codepen.io/GeorgePark/full/VXrwOP/

*/

// const posts = document.querySelectorAll('.gallery-item');

// posts.forEach(post => {
// 	post.addEventListener('click', () => {
// 		//Get original image URL
// 		const imgUrl = post.firstElementChild.src.split("?")[0];
// 		//Open image in new tab
// 		window.open(imgUrl, '_blank');
// 	});
// });
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
if (event.target == modal) {
modal.style.display = "none";
}
}

var modal2 = document.getElementById("myModal2");

// Get the button that opens the modal
var btn2 = document.getElementById("myBtn2");

// Get the <span> element that closes the modal
var span2 = document.getElementsByClassName("close2")[0];

// When the user clicks the button, open the modal 
btn2.onclick = function() {
modal2.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span2.onclick = function() {
modal2.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
if (event.target == modal2) {
modal2.style.display = "none";
}
}

var modal3 = document.getElementById("myModal3");

// Get the button that opens the modal
var btn3 = document.getElementById("myBtn3");

// Get the <span> element that closes the modal
var span3 = document.getElementsByClassName("close3")[0];

// When the user clicks the button, open the modal 
btn3.onclick = function() {
modal3.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span3.onclick = function() {
modal3.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
if (event.target == modal3) {
modal3.style.display = "none";
}
}

var modal4 = document.getElementById("myModal4");

// Get the button that opens the modal
var btn4 = document.getElementById("myBtn4");

// Get the <span> element that closes the modal
var span4 = document.getElementsByClassName("close4")[0];

// When the user clicks the button, open the modal 
btn4.onclick = function() {
modal4.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span4.onclick = function() {
modal4.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
if (event.target == modal4) {
modal4.style.display = "none";
}
}

var modal5 = document.getElementById("myModal5");

// Get the button that opens the modal
var btn5 = document.getElementById("myBtn5");

// Get the <span> element that closes the modal
var span5 = document.getElementsByClassName("close5")[0];

// When the user clicks the button, open the modal 
btn5.onclick = function() {
modal5.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span5.onclick = function() {
modal5.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
if (event.target == modal5) {
modal5.style.display = "none";
}
}
