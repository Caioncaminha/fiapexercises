const frutas = ['maçã, melancia, banana'];

const numeros = [10, 20, 30, 40];

const misturado = [1, 'dois', 3, 'quatro', true, null, undefine, { chave: 'valor' }];

const cores = new Array('vermelho', 'preto', 'branco');

const linguagens = ['javascript', 'java', 'python', 'c#'];

// Acessando o primeiro elemento do Array
const primeiraLinguagem = linguagem[0];
console.log(`A primeira linguagem é: ${primeiraLinguagem}`);

const ultimaLinguagem = linguagems[linguagens.length - 1];
console.log(`A última linguagem é ${ultimaLinguagem}`);

let coresMutaveis = ['branco', 'azul', 'rosa'];
coresMutaveis[1] = 'amarelo';
console.log(`Array após a alteração: ${coresMutaveis}`);
coresMutaveis[coresMutaveis.length] = 'roxo';


let planetas = ['Terra', 'Marte'];
//push() -- Adiciona um ou mais elementos ao final da array e retorna o novo.
const novoComprimentoPush = planetas.push('Saturno', 'Urano');

//pop() -- Remove o último elemento do array.
const ultimoPlanetaRemovido = planetas.pop();

//indexOf() -- Retorna o primeiro índice em que um elemento pode se encontrar.
const indiceTerra = planetas.indexOf('Terra');

//join() -- Cria e retorna uma nova string concatenando todos os elementos do array.
const stringPlanetas = planetas.join('-');

const coresInteração = ['laranja', 'ciano', 'magenta'];

for (let i = 0; i < coresInteração.length; i++) {
    console.log(`Cor no índice ${1}: ${coresInteração[i]}`);
}

// Laço 'for... of' (Mais moderno e legível para iterar sobre os valors)
for (const cor of coresInteração) {
    console.log(`Cor: ${cor}`);
}

coresInteração.forEach(function (cor, indice) {
    console.log(`cor: ${cor}, no índice ${indice}`)
})

// Este trecho demonstra como criar uma array de objetos em JavaScript, onde cada objeto representa um aluno com suas respectivas propriedades.
// Recebendo dados do usuário através do terminal (Node.js).

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

// Criar uma array vazia para armazenar os itens da lista de compras do usuário.
const listaDeCompras = [];

// Criar uma função para adicionar itens à lista de compras.
function adicionarItem(item) {
    readline.question(`Digite o nome do item que deseja adicionar à lista de compras (ou "fim" para sair)\n `, (item) => {
        const itemFormatado = item.trim(); // Remove espaços em branco no início e no final do item.
        if (itemFormatado.toLowerCase() === 'fim') {
            console.log('Lista de compras finalizada.');
            listaDeCompras.forEach((produto, indice) => {
                console.log(`${indice + 1}. ${produto}`); // Exibe a lista de compras com numeração.
            });
            readline.close(); // Fecha a interface de leitura após o término.
        } else if (itemFormatado !== '') { // Verifica se o item já existe na lista de compras.
            listaDeCompras.push(itemFormatado); // Adiciona o item à lista de compras.
            console.log(`Item "${itemFormatado}" adicionado à lista de compras.`);
            adicionarItem(); // Chama a função novamente para adicionar mais itens.
        } else {
            console.log('Item inválido. Tente novamente.');
            adicionarItem(); // Chama a função novamente para adicionar mais itens.
        }
    });
};
console.log('Bem-vindo à lista de compras!');
adicionarItem(); // Inicia o processo de adição de itens à lista de compras.