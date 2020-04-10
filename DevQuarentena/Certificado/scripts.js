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
    }

    listaL = [
        "https://codepen.io/plaisteixo-5/pen/dyoLZBo",
        "https://onepieceex.net/"
    ];
    titulos = [
        "Sorteio",
        "One Piece"
    ]

    cont = 0;

    while(cont < 2){
        listaLink = listaLink + `<li>${titulos[cont]}: <a target="_blank" href="${listaL[cont]}">${listaL[cont].replace("https://","")}</a></li>`;
    
        cont++;
    };
    
    document.body.innerHTML = `${certificadoH}
    <ol>
        ${listaLink}
    </ol>
    `;
};