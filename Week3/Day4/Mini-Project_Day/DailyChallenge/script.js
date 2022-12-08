const tasks = [];
document.querySelector("button").addEventListener("click", addTask)

function addTask(event) {
    event.preventDefault();
    let input1 = document.forms[0].firstInput;
    if (input1.value !== "") {
        let newTask=createNewTask(input1);
        document.querySelector(".listTasks").appendChild(newTask);
        input1.value = ""; //cleaning the input
    }else{
        alert("please type a task to add")
    }
}

function createNewTask(input1){
    let newTask = document.createElement("div");
        newTask.classList.add("newTask")
        let btnX = document.createElement("button");
        btnX.classList.add("buttonX");
        btnX.textContent="x";
        let newInput = document.createElement("input");
        newInput.classList.add("newInput");
        newInput.type="checkBox";
        let label=document.createElement("label");
        label.textContent = input1.value;
        newTask.append(btnX, newInput,label);
        return newTask;
}