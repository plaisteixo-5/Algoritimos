var quant = 0;
function adicionarLike(){
    if (quant == 0){
        quant = 1+quant;
        botao.innerHTML = quant + " Like"
        // alert(quant+"Like")
    } else{
        quant = 1+quant;
        botao.innerHTML = quant + " Likes"
        // alert(quant+"Likes")
    };
};