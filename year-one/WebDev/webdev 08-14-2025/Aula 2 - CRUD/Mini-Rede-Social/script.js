// Dados de exemplo dos posts
let posts = [
    {
        text: "Este é o primeiro post",
        category: "Notícias",
        image: "https://placedog.net/150?random=1",
        date: "12/10/2021 12:00:00"
    },
    {
        text: "Este é o segundo post",
        category: "Dicas",
        image: "https://placedog.net/150?random=2",
        date: "12/10/2022 12:00:00"
    },
    {
        text: "Este é o terceiro post teste",
        category: "Eventos",
        image: "https://placedog.net/150?random=3",
        date: "12/10/2023 12:00:00"
    }
];

// const pessoa = {
//     nome: 'Caio',
//     idade: 32,
//     "Cidade Natal": "São Paulo",
//     isAdmin: true

// }

// console.log(pessoa.nome)
// console.log(pessoa[nome])

window.onload = function(){
    mostrarPosts()
    document.querySelector("postForm").addEventListener("submit", addPost)
}

// CREATE
function addPost(){}
    infosDoEvento.preventDefault();

    const textoPost = document.querySelector("#postText").value;
    const categoriaPost = document.querySelector("#postCategory").value;
    const imagemPost = document.querySelector("#postImage").value;
    const dataPost = new Date().toLocaleString();
    
// READ
function mostrarPosts(){
    const listaPosts = document.querySelector("#postList")
    listaPosts.innerHTML = ""

    posts.forEach(pegaItem => {
        const cardPost = document.createElement("div")
        cardPost.classList.add("card")

        cardPost.innerHTML = `
        <h2>${pegaItem.text}</h2>
        <img src="${pegaItem.image}"/>
        <p></p>
        `

        listaPosts.append(cardPost)
    })
}

// UPDATE
function editarPost(){}
// DELETE
function deletarPost(){}
