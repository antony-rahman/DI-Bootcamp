// // Exercise 1 - basic add event listener

// // Create two buttons - id of "red", id of "blue"
// // When we click on the red button -> Change the backgroundcolor of the page to red
// // When we click on the blue button -> Change the backgroundcolor of the page to blue

// const firstBtn = document.getElementById("btnOne");
// const secondBtn = document.getElementById("btnTwo");

// firstBtn.addEventListener("click", alertUser);
// secondBtn.addEventListener("click", alertUserTwo);

// function alertUser(){
//     document.body.style.backgroundColor = "blue";
// }

// function alertUserTwo(){
//     document.body.style.backgroundColor = "red";
// }

// Exercise 2 - using the event object

const colors = ["blue", "yellow", "green", "pink"];

// Add inside the HTML file a div of id "container" (do it directly in the HTML)
// Add one button per color inside the div container (do it directly in the JS)

function colorsloop(){

for (let cOlOr of colors){
    const btn = document.createElement("button");
    btn.textContent = cOlOr;
   btn.addEventListener("click",)
}
}
colorsloop()


// Each button should have an "click" event listener that changes the background color of the document, to the text content of the button (do it directly in the JS)

// Exercise 3 - Pictures

// const pics = [ "https://images.pexels.com/photos/1741205/pexels-photo-1741205.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" "https://images.pexels.com/photos/2253275/pexels-photo-2253275.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" "https://images.pexels.com/photos/3439576/pexels-photo-3439576.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" ];

// Using this array, create a button on the page that when clicked on display 3 animals photo, but the order of the picture should be random
// Set a class to the image, so each image will be 200px height, and width, and in the middle of the page
// Add a button next to each image
// When we click on one image, it should disapear(ie. be deleted),
// When we hover on the image, it should display the "alt".