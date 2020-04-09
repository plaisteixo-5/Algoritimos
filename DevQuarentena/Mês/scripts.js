nM = prompt("Digite o número de um mês do ano: ");

if(nM == 1){
    mes = "Janeiro";
} else if(nM == 2){
    mes = "Fevereiro";
} else if(nM == 3){
    mes = "Março";
} else if(nM == 4){
    mes = "Abril";
} else if(nM == 5){
    mes = "Maio";
} else if(nM == 6){
    mes = "Junho";
} else if(nM == 7){
    mes = "Julho";
} else if(nM == 8){
    mes = "Agosto";
} else if(nM == 9){
    mes = "Setembro";
} else if(nM == 10){
    mes = "Outubro";
} else if(nM == 11){
    mes = 'Novembro';
} else if(nM == 12){
    mes = 'Dezembro';
};

tagP.innerHTML = 'O mês equivalente ao número que você digitou é '+mes;