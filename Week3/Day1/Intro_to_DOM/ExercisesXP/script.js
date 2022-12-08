// const firstDiv = document.body.children[0]
// const divOne = document.body.firstElementChild;
// console.log(divOne);
// //ul

// const firstUL = document.body.children[1];
// const ulOne = firstDiv.firstElementChild;

// //second li "Pete"

// const secondLi = firstUL.children[1];
// const LiTwo = firstUL.lastElementChild;

// LiTwo.textContent = "Richard";

// console.log(LiTwo);

// const secondUL = document.body.children[2];


// console.log(secondUL);

// const LiOne = firstUL.children[0]
// LiOne.textContent = "Anton"

// const SndLiOne = secondUL.children[0]
// SndLiOne.textContent = "Anton"

// const trdLiOne = secondUL.children[1]
// secondUL.removeChild(trdLiOne)








// document.body.firstElementChild.style.backgroundColor = "lightblue";
// document.body.firstElementChild.style.padding = "50px";
// document.body.style.fontSize = "x-large";

// const li1 = document.body.children[1];



// const liChild = li1.children[0];    

// const liChild2 = li1.children[1];



// liChild.style.display = "none";

// liChild2.style.border = "thick solid #0000FF";





// const div1 = document.body.firstElementChild;
// div1.setAttribute("id", "socialNetworkNavigation");
// console.log(div1);

// const createdlist = document.createElement("li");
// const createdtext = document.createTextNode("Logout");
// createdlist.appendChild(createdtext);
// const uList = div1.firstElementChild;

// uList.appendChild(createdlist);


const allBooks=[
    {title: 'Chainsaw Man',
    author: 'Tatsuki Fujimoto',
    image: new URL('https://static.wikia.nocookie.net/chainsaw-man/images/0/0f/Volume_01.png/revision/latest?cb=20190226192508'),
    alreadyRead: true
},
{
    title: 'Sphere',
    author: 'Michael Crichton',
    image: new URL('https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1660273071i/455373._UY1220_SS1220_.jpg'),
    alreadyRead: true
}
];



const tableBooks=document.createElement('table');
const divBooks=document.querySelector('div');
divBooks.appendChild(tableBooks);
for(book of allBooks){
    let tr= document.createElement('tr')
    tableBooks.appendChild(tr);
    for(book1 in book){
        let td=document.createElement('td');
        document.querySelector('tr').appendChild(td);
        td.innerText= book.author
    }
}
