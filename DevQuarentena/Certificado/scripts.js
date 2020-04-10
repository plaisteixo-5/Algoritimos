var certificadoH;
var link;
var listaL = "";
var cont;
var listaLink = "";
var titulos = "";

function gerar(){
    i = 0;
    while (i < 1000000){
        i += 1;
        certificadoH = emitirCertificado(inputNome.value);
    }// Libera uma condição do certificado

    listaL = [
        "https://codepen.io/plaisteixo-5/pen/dyoLZBo",
        "https://onepieceex.net/"
    ];
    titulos = [
        "Sorteio",
        "One Piece"
    ]//listaL e titulos são variáveis vetoriais que comportam todos os nomes e links que quiser colocar

    cont = 0;

    while(cont < 2){
        listaLink = listaLink + `<li>${titulos[cont]}: <a target="_blank" href="${listaL[cont]}">${listaL[cont].replace("https://","")}</a></li>`;
    
        cont++;
    };// esse while serve para organizar a listaLink com todos os nomes e links
    
    document.body.innerHTML = `${certificadoH}
    <ol>
        ${listaLink}
    </ol>
    `;//Esse trecho printa as coisas na tela
};