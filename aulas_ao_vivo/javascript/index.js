//Criar os elementos // 
const article = document.createElement("article")
console.log(article);
//manipular elementos//
article.innerHTML = `<h3>Pop Vegan </h3>
<p class="subtitulo"> `;
// Renderizar os elementos na página/ Adicionar no DOM//
const main = document.querySelector('main');
main.appendChild(article)
article.id = "post-02"
const id = article.setAttribute("id", "post-02")
// Popup +//
usernameInput.addEvenListener("focus", () => {
    usernameLabel.classList.add('required-popup')
});

// Popup -//
usernameInput.addEvenListener("focus", () => {
    usernameLabel.classList.remove("required-popup")
});

