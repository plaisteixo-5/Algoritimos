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
        "https://codepen.io/plaisteixo-5/pen/jOPjNqJ",
        "https://codepen.io/plaisteixo-5/pen/MWwROBX",
        "https://codepen.io/plaisteixo-5/pen/VwvYVNz"
    ];
    titulos = [
        "Sorteio",
        "Curriculo",
        "Calculadora de Corrida",
        "Botão de Like"
    ]//listaL e titulos são variáveis vetoriais que comportam todos os nomes e links que quiser colocar

    cont = 0;

    while(cont < 4){
        listaLink = listaLink + `
        <li>
            <a target="_blank" href="${listaL[cont]}">${titulos[cont]}
            </a>
        </li>`;
    
        cont++;
    };// esse while serve para organizar a listaLink com todos os nomes e links
    
    document.body.innerHTML = `${certificadoH}
    <ol>
        ${listaLink}
    </ol>
    `;//Esse trecho printa as coisas na tela
};