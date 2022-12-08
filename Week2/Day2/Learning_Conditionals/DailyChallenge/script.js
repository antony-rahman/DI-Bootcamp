// // 🌟 Exercise 1: Simple If/Else Statement
// // Instructions
// // Create 2 variables, x and y. Each of them should have a different numeric value.
// // Write an if/else statement that checks which number is bigger.

// let x = 1;

// let y = 9;

// if (x < y){console.log("x is smaller than y")}
// else{console.log("x is larger than y")};

// // 🌟 Exercise 2: Chihuahua
// // Instructions
// // Create a variable called newDog where it’s value is “Chihuahua”.
// // Check and display how many letters are in newDog.
// // Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
// // Check if the variable newDog is equal to “Chihuahua”
// // if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
// // else, console.log ‘I dont care, I prefer cats’

// let newDog = "Chihuahua";
// const letterCount = newDog.length;

// console.log(letterCount);

// console.log(newDog.toUpperCase());

// console.log(newDog.toLowerCase());

// if (newDog == "Chihuahua"){console.log("I love Chihuahuas, its my favorite breed.")}
// else{console.log("I dont care, I prefer snakes.")};

// // 🌟 Exercise 3: Even Or Odd
// // Instructions
// // Prompt the user for a number and save it to a variable.
// // Check whether the variable is even or odd.
// // If it is even, display: “x is an even number”. Where x is the actual number the user chose.
// // If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.

// const numInput = window.prompt("Input number");
// if(numInput % 2 == 0){console.log(numInput ," is an even number")}
// else{console.log(numInput, "is an odd number")};

// // 🌟 Exercise 4: Group Chat
// // Instructions
// // Below is an array of users that are online in a group chat.

// // const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
// // Using the array above, console.log the number of users that 
// // are connected to the group chat based on the following rules:
// // If there is no users (the users array is empty), console.log “no one is online”.
// // If there is 1 user, console.log “<name_user> is online”.
// // If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
// // If there are more than 2 users, console.log the first two names in 
// // the users array and the number of additional users online.
// // For example, if there are 5 users, it should display:
// // name_user1, name_user2 and 3 more are online

// const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000" , "FatAlbert"];

// const usersOn = users.length;

// if(usersOn == 0){console.log("no one is online")};
// if (usersOn == 1) {console.log(users[0] ," is online")};
// if (usersOn == 2) {console.log(users[0] ," and" , users[1] , " are online")};
// if (usersOn > 2) {console.log(users[0] ,"," , users[1] , " and " , usersOn - 2 , "more are online")};



//=========================================================


// Instructions
// Create a variable called sentence. The value of the variable should be a 
// string that contains the words “not” and “bad”.
// For example, “The movie is not that bad, I like it”.

// Create a variable called wordNot where it’s value is the first appearance 
// (ie. the position) of the substring “not” (from the sentence variable).

// Create a variable called wordBad where it’s value is the first appearance 
// (ie. the position) of the substring “bad” (from the sentence variable).

// If the word “bad” comes after the word “not”, you should replace the 
// whole “not…bad” substring with “good”, then console.log the result.
// For example, the result here should be : “The movie is good, I like it”
// If the word “bad” does not come after “not” or the words are not in the 
// sentence, console.log the original sentence.
// Example:

//   Your string is : 'This dinner is not that bad ! You cook well', 
//   --> the result is : 'This dinner is good ! You cook well'

//   Your string is : 'This movie is not so bad !' 
//   --> the result is : 'This movie is good !'

//   Your string is : 'This dinner is bad !' 
//   --> the result is : 'This dinner is bad !'

const sentence = `This bootcamp is not the best in the world, but also cant say its bad, I like it`

const wordNot = sentence.search("not");

const wordBad = sentence.search("bad");

if (wordNot === -1){console.log(sentence)}
else 
if (wordNot < wordBad) {

const sentence1 = sentence.slice(0, wordNot)
const sentence2 = sentence.slice(wordBad + 3)

console.log(sentence1 + "good" + sentence2);
} 
else console.log(sentence);