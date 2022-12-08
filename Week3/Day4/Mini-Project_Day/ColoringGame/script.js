var main = document.getElementById('middle');
var left = document.getElementById('left');
var cells = document.getElementsByClassName('cell');
var palette = document.getElementsByClassName('palette');
var body = document.getElementsByTagName('body')[0];
var button = document.getElementsByTagName('button')[0];
var color = null;



//create cells for coloring
for (i=0; i<1440; i++) {
    let div = document.createElement("div");
    div.className = "cell";
    main.appendChild(div);
}

//create color palette
for (let i = 0; i<21; i++) {
    let div = document.createElement('div');
    div.className = "palette";
    div.style.backgroundColor = specificColor();
    left.appendChild(div);
}

// //assign a random color to palette 
// function randomColor (){
//     let letters = '0123456789ABCDEF';
//     let color = '#'
//     for (let i=0; i<6; i++) {
//         color += letters[Math.floor(Math.random()*16)]
//     }
//     return color
// }

//manually assign specific colors to palette
function specificColor(){
let colorsForPalette = ["red", "orangered", "orange", "yellow", "yellowgreen", "lightgreen", "green", "turquoise", "cyan", "lightskyblue", "dodgerblue", "blue", "darkblue", "indigo", "darkmagenta", "violet", "lightpink", "lightgray", "gray", "white", "black"];
for (i=0; i<palette.length; i++) {
    palette[i].style.backgroundColor = colorsForPalette[i];
    }
}


//assinging color to "color" when clicking on palette
for (x of palette) {
    x.addEventListener("click", function(event){
        color = event.target.style.backgroundColor;
    });
}

//creating condition to paint only when mouse is pressed
body.addEventListener("mousedown", function(){
    mousedown = true;
})

body.addEventListener("mouseup", function(){
    mousedown = false;
})

//coloring the cells
for (x of cells){
    x.addEventListener("mousedown", function(event){
        event.target.style.backgroundColor = color;
    })
    x.addEventListener("mouseover", function(event){
        if (mousedown){
            event.target.style.backgroundColor = color;
        }
    })
}
//making button clear all color
button.addEventListener("click", function(){
    for (x of cells) {
        x.style.backgroundColor = "white";
    }
});