console.log('Aparece mensagem')
// var myHeading = document.querySelector('h1');
// myHeading.textContent = 'Hello world!';

// var caneta;
// caneta = prompt('Discovery the secret word:');
// if(caneta == 'Tinta'){
//     alert('Yay, i love use pen!');
// }
// else{
//     alert('Ohh, isnt a pen :(');
// }

function multiply(num1,num2) {
    var result = num1 * num2;
    return result;
}

// document.querySelector('html').onclick = function() {
//     alert('Ouch! Stop poking me!');
// }

var imgClick = document.querySelector('img');
imgClick.onclick = function(){
    var meuAlgo = imgClick.getAttribute('src');
    if(meuAlgo === 'caraDeB.png'){
        imgClick.setAttribute('src','yodaDlc.jpg');
    }
    else{
        imgClick.setAttribute('src','caraDeB.png');
    }
}

var myButton = document.querySelector('button');
var myHeading = document.querySelector('h1');

if(!localStorage.getItem('name')){
    setUserName();
}
// else{
//     var storedName = localStorage.getItem('name');
//     myHeading.textContent = 'Mozilla is cool, ' + storedName;
// }

// function setUserName(){
//     var myName = prompt('Digite seu nome: ');
//     localStorage.setItem('name',myName);
//     myHeading.textContent = 'Mozilla is cool, '+myName;
// }

// myButton.onclick = function(){
//     setUserName();
// }


// document.querySelector('img').onclick = function(){
//     alert('Sou lindo né?');
// }