for(let star=1; star<=6; star++){
    console.log("* ".repeat(star));
 }


console.log("=========================");


const n = 6
let star2 = "";
for (let x = 0; x < n; x++) {
    star2 = "";
    for (let y = 0; y <= x; y++) {
        star2 = "* " + star2;
    }
    console.log(star2);
    }