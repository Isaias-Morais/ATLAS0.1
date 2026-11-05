import {accessToken, fazerLogin} from "./auth.js";
import {enviaComandos} from "./api.js";

const formulario = document.getElementById("login-form");

formulario.addEventListener("submit", async function (event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const token = await fazerLogin(email, password);

        if (token) {
            localStorage.setItem("accessToken", token);
            console.log(token);
            window.location.href = "./index.html";
        } else {
            alert("Login Failed")
        }
    } catch (error) {
        console.error(error);
        alert("Login Failed")
    }
});