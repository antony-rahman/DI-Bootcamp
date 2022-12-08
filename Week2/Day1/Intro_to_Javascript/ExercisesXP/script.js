// Exercise 1: Your Favorite Food
// Instructions
// Store your favorite food into a variable.

// Store your favorite meal of the day into a variable (ie. breakfast, lunch or dinner)

// Console.log I eat <favorite food> at every <favorite meal>

// For example

// If your favorite food is "chocolate", 
// and your favorite meal of the day is "dinner", 
// you will console.log 
// I eat chocolate at every dinner

const FavFood = "omlettes";

const FavMeal = "breakfast";

const Food = `I eat ${FavFood} at every ${FavMeal}`;


// Exercise 2 : Series
// Instructions


// Part I
// Using this array : const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

// Create a variable named myWatchedSeriesLength that is equal to the number of series in the myWatchedSeries array.

// Create a variable named myWatchedSeriesSentence, that is equal to a sentence describing the series you watched
// For example : black mirror, money heist, and the big bang theory

// Console.log a sentence using both of the variables created above
// For example : I watched 3 series : black mirror, money heist, and the big bang theory





let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

let myWatchedSeriesLength = myWatchedSeries.length;

let myWatchedSeriesSentence = `${myWatchedSeries[0]}, ${myWatchedSeries[1]} and ${myWatchedSeries[2]}`;

let SeriesSentence = `I watched ${myWatchedSeriesLength} series : ${myWatchedSeriesSentence}`;

console.log(SeriesSentence);

// Part II
// Change the series “the big bang theory” to “friends”. Hint : You will need to use the index of “the big bang theory” series.
// Add, at the end of the array, the name of another series you watched.
// Add, at the beginning of the array, the name of your favorite series.
// Delete the series “black mirror”.
// Console.log the third letter of the series “money heist”.
// Finally, console.log the myWatchedSeries array, to see all the modifications you’ve made.

myWatchedSeries[2] = "friends";

myWatchedSeries.push("walking dead");

myWatchedSeries.unshift("Edgerunners"); 



// let array1 = myWatchedSeries.splice(0,1);
// let array2 = myWatchedSeries.splice(1);
// myWatchedSeries = array1.concat(array2);

myWatchedSeries.splice(1,2);


console.log(myWatchedSeries[1][2]);
console.log(myWatchedSeries)

// Exercise 3 : The Temperature Converter
// Instructions
// Store a celsius temperature into a variable.

// Convert it to fahrenheit and console.log <temperature>°C is <temperature>°F.
// Hint : Should you create another variable to hold the temperature in fahrenheit? (ie. point 2)
// Hint: To convert a temperature from celsius to fahrenheit : Divide it by 5, then multiply it by 9, then add 32

let temperatureC = 25
let temperatureF = 77

let conversion = `${temperatureC}°C is ${temperatureF}°F`
console.log(conversion)

// Exercise 4 : Guess The Answers #1
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.



// For example

// console.log(2+3)
// // Prediction: It will output 5, because 2 and 3 are numbers
// // Actual: 5


// Using the code below:

//     let c;
//     let a = 34;
//     let b = 21;

//     console.log(a+b) //first expression
//     // Prediction:
//     // Actual:

//     a = 2;

//     console.log(a+b) //second expression
//     // Prediction:
//     // Actual:



// What will be the outcome of a + b in the first expression ?
// What will be the outcome of a + b in the second expression ?
// What is the value of c?

// Analyse the code below, what will be the outcome?
// console.log(3 + 4 + '5');


    let c;
    let a = 34;
    let b = 21;

//1
    console.log(a+b) //first expression
    // Prediction:55
    // Actual:55

//2
    a = 2;

    console.log(a+b) //second expression
    // Prediction: 23
    // Actual: 23

//3
    
    console.log(c)
    // Prediction:the value of 'c' is undefined.
    // Actual: undefined
//4 

console.log(3 + 4 + '5');
    // Prediction: '5' is a string, value will be 75
    // Actual: 75



//     Exercise 5 : Guess The Answers #2
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.



// For example

// typeof("potato")
// // Prediction: Vegetable
// // Actual: String

typeof(15)
// Prediction:number
// Actual:number

typeof(5.5)
// Prediction:number
// Actual:number

typeof(NaN)
// Prediction:function
// Actual:number

typeof("hello")
// Prediction:string
// Actual:string

typeof(true)
// Prediction:boolean
// Actual:boolean

typeof(1 != 2)
// Prediction:boolean
// Actual:boolean

"hamburger" + "s"
// Prediction:hamburgers
// Actual:hamburgers

"hamburgers" - "s"
// Prediction:hamburger
// Actual:NaN

"1" + "3"
// Prediction:13
// Actual:13

"1" - "3"
// Prediction:NaN
// Actual:-2

"johnny" + 5
// Prediction:johnny5
// Actual:johnny5

"johnny" - 5
// Prediction:NaN
// Actual:NaN

99 * "hello"
// Prediction:NaN
// Actual:NaN

1 != 1
// Prediction:false
// Actual:false

1 == "1"
// Prediction:true
// Actual:true

1 === "1"
// Prediction:false 
// Actual:false




// Exercise 6 : Guess The Answers #3
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.



// What is the output of each of the expressions below?

5 + "34"
// Prediction:534
// Actual:534

5 - "4"
// Prediction:1
// Actual:1

10 % 5
// Prediction:0.5
// Actual:0

5 % 10
// Prediction:0
// Actual:5

"Java" + "Script"
// Prediction:JavaScript
// Actual:JavaScript

" " + " "
// Prediction:
// Actual:'  '

" " + 0
// Prediction:0
// Actual:' 0'

true + true
// Prediction:2
// Actual:2

true + false
// Prediction:1
// Actual:1

false + true
// Prediction:1
// Actual:1

false - true
// Prediction:-1    
// Actual:-1

!true
// Prediction:
// Actual:false

3 - 4
// Prediction:-1
// Actual:-1

    "Bob" - "bill"
// Prediction:NaN
// Actual:NaN

