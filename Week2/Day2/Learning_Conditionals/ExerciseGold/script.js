const answerUser = prompt("what is your language").toLowerCase();

// if (answerUser === "french"){
//     console.log("Bonjour");
// } else if (answerUser === "english"){
//         console.log("Hello");
// } else if (answerUser === "hebrew"){
//     console.log("Shalom");
// } else console.log("01110011 01101111 01110010 01110010 01111001");

switch(answerUser){
    case "french": 
        console.log("Bonjour");
        break;

     case "english": 
        console.log("Hello");
        break;

    case "Hebrew": 
        console.log("Shalom");
        break;

    default: 
        console.log("01110011 01101111 01110010 01110010 01111001");
        break;  
}