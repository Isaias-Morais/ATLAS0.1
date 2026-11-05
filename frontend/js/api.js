import { tocarMusica } from "./music.js";

const accessToken = sessionStorage.getItem("accessToken");



export async function enviaComandos(texto){
    const accessToken = localStorage.getItem("accessToken");
    

    const command = await  fetch("http://127.0.0.1:8000/commands/",{
        method:"POST",
        headers:{
            "Content-Type":"application/json",
            "Authorization": `Bearer ${accessToken}`
        },
        body: JSON.stringify({
            "text": texto
        })
    });
    const dados = await command.json();
    if (dados.tipo === "musica") {
        tocarMusica(dados);
    }

    console.log("Dados da música:", dados.musica_id);
    console.log("Estrutura JSON:", JSON.stringify(dados.musica_id, null, 2));

    console.log("Resposta do Atlas:", dados);


}

