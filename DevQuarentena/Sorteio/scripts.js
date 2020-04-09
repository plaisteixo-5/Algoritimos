
function Sort(){
    // aleatorio = 7;
    aleatorio = Math.round(Math.random()*10);
    nUsuario = prompt('Digite seu número da sorte: ');
    // nCerto = prompt('Digite seu número da sorte: ') == aleatorio;
    // pra usar a função de cima vc tinha q colocar o nCerto dentro do If e ele ia funcionar como bool
    if(nUsuario == aleatorio){
        paragrafoResultado.innerHTML = 'Você ganhou o sorteio!!';
        paragrafoResultado.style.fontColor = "Blue";
    } else if(nUsuario > 10){
        alert(`O número digitado é inválido. Aperte enter e tente novamente: `)
        Sort();
    } else{
        paragrafoResultado.innerHTML = `<br>Não foi dessa vez :(</br>
                                        <br>Você digitou ${nUsuario}</br>
                                        <br>O número certo é ${aleatorio}</br>`;
        paragrafoResultado.style.fontColor = "Yellow";
    }
};