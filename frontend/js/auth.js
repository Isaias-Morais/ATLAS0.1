export let accessToken;

export async function fazerLogin(email,password) {
    const resposta = await fetch("http://127.0.0.1:8000/auth/login", {
        method:"POST",
        headers:{
            "Content-Type":"application/json"
            },
        body: JSON.stringify({
            'email' : email,
            'password' : password,
            })
        });
    const dados = await resposta.json();

    console.log("Token no login:", accessToken);
    console.log("Token salvo:", sessionStorage.getItem("accessToken"));
    console.log("Origem:", window.location.origin);

    accessToken = dados.access_token;
    sessionStorage.setItem("accessToken", accessToken);

    return accessToken;

    }



export async function iniciar() {

}



