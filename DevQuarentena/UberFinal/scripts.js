function calcular(){
    distancia = inputDistancia.value;
    tempo = inputTempo.value;

    valorcorrida = 2 + distancia * 1.4 + tempo  * 0.26;

    botaoCalcular.innerHTML = 'O valor da sua corrida foi de R$ ' + DecimalETroca(valorcorrida);
    // var myP = document.querySelector('p');

    // myP.textContent = "O valor da sua corrida foi de R$ " + valorcorrida.toFixed(2);
}

function DecimalETroca(valor){
    return  valor.toFixed(2).replace(".",",");
}