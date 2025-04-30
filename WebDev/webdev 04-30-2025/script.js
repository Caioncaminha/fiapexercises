//Uso de "for", começo, fim, condicional no meio (incremento ou decrimento)
for (let i = 0; i < 5; i++) {
    console.log(`Número: ${i}`);
}

//Uso de while
let contador = 0;

while (contador < 3) {
    console.log(`Contador está em ${contador}`);
    contador++;
}

//Uso de "for in", criar uma variável para ler e utilizar os dados da array
const pessoa = {
    nome: 'Caio',
    idade: 18,
    cidade: 'São Paulo'
};
for (const dados in pessoa) {
    console.log(`${dados}: ${pessoa[dados]}`);
}

//Uso de "for of", criar uma variável para ler toda a array em ordem
const cores = ['vermelho', 'azul', 'preto'];

for (const cor of cores) {
    console.log(cor);
}

const carro = {
    marca: 'Ford',
    modelo: 'Fusion',
    ano: '2007',
    cor: 'Cinza',
    ligar: function () {
        console.log("O carro está ligado.");
    },


    obterDetalhes: function () { //obterDetalhes é um outro método
        return `${this.marca} ${this.modelo} ${this.ano}`; //"this" se refere a variável "carro"
    }
};

console.log('---Objeto Literal---');
console.log(`Marca: ${carro.marca}`); //Acessando a propriedade "marca" usando "carro" ao invés de "this"
console.log(`Modelo ${carro.modelo}`);
carro.ligar();//Chamando o método ligar usando a notação de ponto

const detalhesCarro = carro.obterDetalhes();
console.log(`Detalhes do carro ${detalhesCarro}`);

console.log("---Exibindo o objeto---")
for (const propriedade in carro) {
    console.log(`${propriedade}: ${carro[propriedade]}`);
}

//Outra forma de exibir um objeto("Converte o objeto para uma string JSON")
const carroJSON = JSON.stringify(carro);