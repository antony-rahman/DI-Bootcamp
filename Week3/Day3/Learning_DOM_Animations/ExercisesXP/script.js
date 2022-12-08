// setTimeout(helloWorld, 2000);
// function helloWorld() {
//     alert(`hello world!`)
// }


// setTimeout(helloWorld2, 1991);
// function helloWorld2() {
//     let pHW = document.createElement("p");
//     pHW.textContent = 'Hello World!';
//     document.getElementById("container").appendChild(pHW);
//     if (document.querySelectorAll('p').length >= 5) {
//         clearInterval(createP);
//     }

// }

// const createP = setInterval(helloWorld2, 2000);
// document.getElementById('clear').addEventListener('click', clearMyInterval);
// function clearMyInterval() {
//     clearInterval(createP);
// }



////////////////////////////////



let move;
let left;
function myMove() {
   move =setInterval(moveRight, 1);
    left = 0;
}
const redSquare = document.getElementById('animate');

function moveRight() {
    if (left<=350) {
        left++;
        redSquare.style.left = `${left}px`;
    } else {
        clearInterval(move);
    }
}
