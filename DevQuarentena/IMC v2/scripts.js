function calcular(){
    p = inputP.value;
    a = inputA.value;
    a = a/100;
    IMC = p/(a*a);
    console.log(IMC);
    if(IMC <= 17){
        pCalcular.innerHTML = 'Seu peso está a baixo do normal, pois seu IMC é de '+printaBagui(IMC);
    } else if(IMC >= 18 && IMC < 24.99){
        pCalcular.innerHTML = 'Seu peso está normal, pois seu IMC é de '+printaBagui(IMC);
    } else if(IMC >= 24.99 && IMC < 29.99){
        pCalcular.innerHTML = 'Seu peso está acima do normal, pois seu IMC é de '+printaBagui(IMC);
    } else if (IMC >= 29.99 && IMC < 34.99){
        pCalcular.innerHTML = 'Você está com obesidade I, pois seu IMC é de '+printaBagui(IMC);
    } else if(IMC >= 35){
        pCalcular.innerHTML = 'Você está com obesidade, pois seu IMC é de '+printaBagui(IMC);
    }
    
};

function printaBagui(IMC){
    result = (IMC).toFixed(2).replace('.',',');
    return result;
}