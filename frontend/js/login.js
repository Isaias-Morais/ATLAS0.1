import {accessToken, fazerLogin} from "./auth.js";

const formulario = document.getElementById("login-form");

formulario.addEventListener("submit", async function (event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const token = await fazerLogin(email, password);

    console.log(token);
});