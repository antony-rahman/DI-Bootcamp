const users = ["John", "Lola", "Tom"];

// for each user 
// create a paragrah
// the text of the paragraph is the name of the user

function addPara () {
    const wrapper = document.getElementById("container"); 
    for (let i = 0; i<users.length; i++){
        const paragraph = document.createElement("p");
        paragraph.classList.add("para"); // add a class called para
        const text = document.createTextNode(`Hello ${users[i]}`);
        paragraph.appendChild(text);
        wrapper.appendChild(paragraph);
    }
}

addPara();

// document.getElementById("container").style.backgroundColor = "blue"
// inline style