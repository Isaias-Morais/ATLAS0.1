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

    return(dados.access_token);

    }



export async function iniciar() {
    const accessToken = await fazerLogin();

}

iniciar();



