
const input1=document.querySelector('input');
input1.addEventListener('keydown',acceptOnlyLetters);

function acceptOnlyLetters(event){
    let actualKey=event.key.toLowerCase();
    if (!(actualKey >= 'a' && actualKey <= 'z')){
        event.preventDefault();
        console.log('oops!');
    }
    
}
