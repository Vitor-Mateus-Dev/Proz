// ---------- VALIDAÇÃO USERNAME ---------- //
let usernameInput = document.getElementById("username");
let usernameLabel = document.querySelector('label[for="username"]');
let usernameHelper = document.getElementById("username-helper");

// Mostrar popup de campo obrigatório
usernameInput.addEventListener("focus", () => {
    usernameLabel.classList.add('required-popup')
});
// Ocultar popup de campo obrigatório
usernameInput.addEventListener("blur", () => {
    usernameLabel.classList.remove('required-popup')
});

// Validar valor do input
