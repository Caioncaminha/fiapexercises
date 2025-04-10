console.log("Script externo rodando para o DOM");

const tituloElemento = document.getElementById('tituloDinamico');
tituloElemento.textContent = "Texto alterado pelo JavaScript";
tituloElemento.style.color = "blue";

const botaoElemento = document.getElementById('meuBotao') //seleciona o botao pelo id
botaoElemento.addEventListener("click", function () {
    alert("Botão foi clicado");
})

