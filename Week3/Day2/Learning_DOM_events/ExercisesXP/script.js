// //Using a DOM property, retrieve the h1 and console.log it.
// const h1=document.querySelector("h1");
// console.log(h1);
// //Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
// const h2=document.querySelector("h2");
// h2.addEventListener('click',changeColorH2);

// function changeColorH2(event){
//     event.target.style.backgroundColor='red';
// }

// //Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
// const h3=document.querySelector("h3");
// h3.addEventListener('click',hideH3);

// function hideH3(event){
//     event.target.style.display='none';
// }

// //Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
// const btnBold=document.querySelector("button");
// btnBold.addEventListener('click',boldText);

// function boldText(){
//     let paras=document.querySelectorAll('p');
//     for (let p of paras) {
//         p.style.fontWeight='bold';
//     }
// }

// //BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)
// h1.addEventListener('mouseover',randomSize);

// function randomSize(event){
//     event.target.style.fontSize=`${Math.round(Math.random()*100)}px`;
// }

// //BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
// const secondP=document.querySelector('p#second');
// secondP.addEventListener('mouseover',fadeOut);
// secondP.addEventListener('mouseout',fadeOut);

// function fadeOut(event){
//     event.target.classList.toggle('fade-out');
// }


// //🌟 Exercise 2 : Work With Forms
// //Retrieve the form and console.log it.
// //Retrieve the inputs by their id and console.log them.
// //Retrieve the inputs by their name attribute and console.log them.
// //When the user submits the form (ie. submit event listener)
// // use event.preventDefault(), why ?
// // get the values of the input tags,
// // make sure that they are not empty,
// // create an li per input value,
// // then append them to a the <ul class="usersAnswer"></ul>, below the form.

// const form1 = document.forms[0];
// console.log(form1);

// let inputFname = document.getElementById('fname');
// console.log(inputFname);
// let inputLname = document.getElementById('lname');
// console.log(inputLname);
// let inputSubmit = document.getElementById('submit');
// console.log(inputSubmit);

// inputFname = document.forms[0].fname;
// console.log(inputFname);
// inputLname = document.getElementsByName('lname')[0];
// console.log(inputLname);
// inputSubmit = document.forms[0].submit;
// console.log(inputSubmit);

// inputSubmit.addEventListener('click', mySubmit);

// function mySubmit(event) {
//     event.preventDefault();
//     let valueFname = inputFname.value;
//     let valueLname = inputLname.value;

//     if (valueFname !== '' && valueLname !== '') {
//         const li1 = document.createElement('li');
//         const li1Text = document.createTextNode(valueFname);
//         li1.appendChild(li1Text);
//         const li2 = document.createElement('li');
//         const li2Text = document.createTextNode(valueLname);
//         li2.appendChild(li2Text);
//         const ul=document.querySelector('ul');
//         ul.appendChild(li1);
//         ul.appendChild(li2);
        
//     }
// }



// //🌟 Exercise 3 : Transform The Sentence
// //Declare a global variable named allBoldItems.
// let allBoldItems;

// //Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.
// function getBold_items(){
//     allBoldItems=document.querySelectorAll("strong");
//     return allBoldItems;
// }

// //Create a function called highlight() that changes the color of all the bold text to blue.
// function highlight(){
//     allBoldItems=getBold_items();
//     for (const strong of allBoldItems) {
//         strong.style.color='blue';
//     }
// }


// //Create a function called return_normal() that changes the color of all the bold text back to black.
// function return_normal(){
//     allBoldItems=getBold_items();
//     for (const strong of allBoldItems) {
//         strong.style.color='black';
//     }
// }

// //Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() on mouseout (ie. when the mouse pointer is moved out of the paragraph). 
// const p=document.querySelector('p');
// p.addEventListener('mouseover',highlight);
// p.addEventListener('mouseout',return_normal);

// //🌟 Exercise 4 : Volume Of A Sphere

// let btnCalc = document.forms[0].submit1;
// btnCalc.addEventListener('click',volumeSphere)

// function volumeSphere(event){
//     event.preventDefault();
//    let rad=Number(document.forms[0].radius.value) ;
//    let volume = 4/3 * Math.PI * Math.pow(rad, 3);
//    document.forms[0].volume.value=volume;
// }


document.getElementById('click').addEventListener('click',btnClick);
document.getElementById('mouseover').addEventListener('mouseover',btnMouseover);
document.getElementById('mouseout').addEventListener('mouseout',btnMouseout);
document.getElementById('dblclick').addEventListener('dblclick',btnDblClick);

function btnClick(){
    document.body.style.backgroundColor='yellow';
}

function btnMouseover(event){
    event.target.style.backgroundColor='red';
}

function btnMouseout(event){
    document.body.style.backgroundColor='pink';
}

function btnDblClick(event){
    document.body.style.backgroundColor='red';
}
