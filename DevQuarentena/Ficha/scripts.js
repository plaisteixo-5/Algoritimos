nome = prompt("Digite seu nome: ");
nasc = prompt("Digite sua data de nascimento: ")
idade = prompt("Digite sua idade: ")
preC = confirm("Tem condição pré-existente?")

if(preC){
    aux = "Sim"
}
else{
    aux = "Não"
}
tagh1.innerHTML = 'Nome: ' + nome;

lista.innerHTML = 
    `<li>Data de nascimento: ${nasc}</li>
    <li>Idade: ${idade} anos</li>
    <li>Tem condição pré-existente: ${aux}</li>
    <li>Precisa de acompanhamento médico</li>`;