function playTheGame(){
    let popuptext = "Do you want to play a game?"
      if (confirm(popuptext) == false) {
        alert("Regrettable.") 
    } else {
        let numberPrompt = prompt("Please enter a number");
        let numberCheck = isNaN(numberPrompt);
        if (numberCheck == true){alert("Not a number, goodbye")}
        else if (numberPrompt >= 0 && numberPrompt <=10)
        {
            let computerNumber = Math.floor((Math.random() * 10))
            compareNumbers(numberPrompt, computerNumber)
        }else {alert("wrong number, goodbye")}
        
        } 

        
}
    
function compareNumbers(val1, val2){
    console.log(val1, val2)
    let index = 0;
    while(index < 3){

        

        if(val1 == val2){
            alert("winner")
            return
        }
        else if(val1 < val2){
            alert("your number is smaller, try again")
            val1 = prompt("Please enter a number");
        }
        else if(val1 > val2){
            alert("your number is bigger, try again")
            val1 = prompt("Please enter a number");
        }
        else if(index === 2){
            alert("too many attempts " + val2)
            return
        }
        
       
        index++
        
    }
   

    console.log(val1,val2)
    if (val2 === val1){
        alert("WINNER")
    }
    else if (val2 > val1){
        alert("Your number is too small"); 
        let numberPrompt = prompt("Please enter a number");
        let numberCheck = isNaN(numberPrompt);
        if (numberCheck == true){
            alert("Not a number, goodbye")
        }
        else if (numberPrompt >= 0 && numberPrompt <=10){
          
        }
        else {
            alert("wrong number, goodbye")
        }
    }
    else if (val2 < val1){alert("Your number is too big"); let numberPrompt = prompt("Please enter a number");
            let numberCheck = isNaN(numberPrompt);
            if (numberCheck == true){alert("Not a number, goodbye")
                            }
            else if (numberPrompt >= 0 && numberPrompt <=10){

                        }else {alert("wrong number, goodbye")}}


}

