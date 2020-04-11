function calcular(){
    distancia = inputD.value;
    tempo = inputT.value;
    valorcorrida = 2 + distancia * 1.4 + tempo  * 0.26;
    resultP.innerHTML = 'O valor da corrida foi de R$'+valorcorrida.toFixed(2).replace('.',',');
    resultP.style.border = "2px inset rgb(255, 86, 86)";
};

// distancia = prompt("Qual a distância que você andou com o passageiro ou passageira?");
// tempo = prompt("Qual foi o tempo da viagem?");
// document.write("O valor da sua corrida foi: R$ " + valorcorrida.toFixed(2));

// document.write("<body style=background-image:url(https://image.freepik.com/vetores-gratis/mapa-de-ruas-com-pinos-e-rotas_23-2147622544.jpg);>" + "<p>Sua corrida deu R$:" , valorcorrida.toFixed(2) , "</p>" + "</body>")

// var myP = document.querySelector('p');

// myP.textContent = "O valor da sua corrida foi de R$ " + valorcorrida.toFixed(2);

// Três formas de printar o valor 