var numberOfstudnetsEjected=0

function sayHi() {
    alert("kick out remainder");
    alert("who?");
}

function ejectstudent() {
    numberOfstudnetsEjected +=1;
    displayconsole();
    displayejected();
}
 function displayejected() {
    numberOfstudnetsEjected += 1;
    alert('the number of: '+numberOfstudnetsEjected);
 }

 function displayconsole() {
    prompt("give me a number", 7);
 }