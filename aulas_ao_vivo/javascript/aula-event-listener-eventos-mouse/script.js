let quantidadeSubtotal = document.getElementById("quantidade-subtotal");
let valorSubtotal = document.getElementById("valor-subtotal");

let subtotalInfo = {
  quantidade: 1,
  valor: 11.66,
};

quantidadeSubtotal.innerText = subtotalInfo.quantidade + " itens";
valorSubtotal.innerText = subtotalInfo.valor;

let botãoAdd = document.getElementById("btn-adicionar-produto-01")
let inputQuantidade = document.getElementById("quantidade-produto-01")
let botãoDim = document.getElementById("btn-subtrair-produto-01")

function  adicionarUm(){
inputQuantidade.value++
}

botãoAdd.addEventListener("click", adicionarUm)

function diminuirUm(){
inputQuantidade.value--
}
botãoDim.addEventListener("click", diminuirUm)