// 🌟 Exercise 1 : List Of People
// Instructions
// const people = ["Greg", "Mary", "Devon", "James"];


// Part I - Review About Arrays
// Write code to remove “Greg” from the people array.

// Write code to replace “James” to “Jason”.

// Write code to add your name to the end of the people array.

// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method

// Write code that gives the index of “Foo”. Why does it return -1 ?

// Create a variable called last which value is the last element of the array.


let people = ["Greg", "Mary", "Devon", "James"];
people.shift();
console.log(people)

people[3]="Jason"
console.log(people)


people.push("Anton");
console.log(people)


var index = people.indexOf("Mary");
console.log(index)

people.splice(0,1);
people.splice(3,1);
console.log(people)


var index1 = people.indexOf("Foo");
console.log(index1)

var last= people[people.length -1]
console.log(last)


// Part II - Loops
// Using a loop, iterate through the people array and console.log each person.

// Using a loop, iterate through the people array and exit the loop after you console.log “Jason” .


for (let i = 0; i < people.length; i++){
    if (i === "Jason"){
        break;
    }
    console.log(people[i])
}



// 🌟 Exercise 2 : Your Favorite Colors
// Instructions
// Create an array called colors where the value is a list of your five favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .


let colors =["crimson", "red" ,"vermillion" ,"purple" ,"pink"];
;
for (let i = 0; i < colors.length; i++){
        let index = colors.indexOf(colors[i+1])
        var sentence = (`My #${index} choice is ${colors[i]}`);
        console.log(sentence)
}


// 🌟 Exercise 4 : Building Management
// Instructions:
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }
// Review About Objects
// Copy and paste the above object to your Javascript file.

// Console.log the number of floors in the building.

// Console.log how many apartments are on the floors 1 and 3.

// Console.log the name of the second tenant and the number of rooms he has in his apartment.

// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.



const building = {
        numberOfFloors: 4,
        numberOfAptByFloor: {
            firstFloor: 3,
            secondFloor: 4,
            thirdFloor: 9,
            fourthFloor: 2,
        },
        nameOfTenants: ["Sarah", "Dan", "David"],
        numberOfRoomsAndRent:  {
            sarah: [3, 990],
            dan:  [4, 1000],
            david: [1, 500],
        },
    }
console.log(building.numberOfFloors);

console.log(building.numberOfAptByFloor.firstFloor);

console.log(building.numberOfAptByFloor.thirdFloor);

console.log(building.numberOfRoomsAndRent.dan[0]);

const sarahAndDavid = (building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]);
let danRent= building.numberOfRoomsAndRent.dan[1];

if (sarahAndDavid > danRent){
    danRent = danRent + 200
    console.log(danRent)
}
else {

}





// 🌟 Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.

const family = {
    mother: " Tanya",
    father: " Lutfar",
    son: " Anton"
 };


 let key = family.property;
 for (let x in family.property){
    key += family.property[x];
 }
 console.log(key);


let object = "";
for (let x in family){
   object += family[x];
}
console.log(object);



// Exercise 6 : Rudolf
// Instructions
// const details = {
//   my: 'name',
//   is: 'Rudolf',
//   the: 'raindeer'
// }
// Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”



const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

let sentence3 = " "
for(const key in details){
    sentence3 = sentence3 + " " + key + " " + details[key]
}
console.log(sentence3)



// Exercise 7 : Secret Group
// Instructions
// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”

const secretnames = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let acronym = ""
const sortedArray = secretnames.sort()

for(const name of sortedArray){
    console.log(name)
    acronym = acronym + name[0]
}
console.log(acronym) 