
import { enviaComandos } from "./api.js";

console.log("Atlas JS conectado");

const reconhecimento = new (
    window.SpeechRecognition || window.webkitSpeechRecognition
)();

reconhecimento.lang = "pt-BR";
reconhecimento.continuous = true;
reconhecimento.interimResults = false;

let atlas_ativo = false;
let processando = false;

function falar(texto) {
    const fala = new SpeechSynthesisUtterance(texto);
    fala.lang = "pt-BR";

    fala.onend = () => {
        if (!processando) {
            iniciarEscuta();
        }
    };

    speechSynthesis.speak(fala);
}

function iniciarEscuta() {
    try {
        reconhecimento.start();
    } catch (erro) {
        console.log("A escuta já está iniciada.");
    }
}

reconhecimento.onstart = () => {
    console.log("Atlas está escutando...");
};

reconhecimento.onresult = async (event) => {
    const indice = event.results.length - 1;
    const texto = event.results[indice][0]
        .transcript.toLowerCase()
        .trim();

    if (!event.results[indice].isFinal) return;

    console.log("Você disse:", texto);

    if (!atlas_ativo) {
        if (texto === "atlas" || texto.startsWith("atlas ")) {
            atlas_ativo = true;

            const comando = texto
                .replace(/^atlas[\s,]*/, "")
                .trim();

            reconhecimento.stop();

            if (comando) {
                await executarComando(comando);
            } else {
                falar("Pode falar");
            }
        }

        return;
    }

    reconhecimento.stop();
    await executarComando(texto);
};

async function executarComando(texto) {
    processando = true;

    try {
        console.log("Enviando comando:", texto);
        await enviaComandos(texto);
    } catch (erro) {
        console.error("Erro ao executar comando:", erro);
        falar("Não consegui executar esse comando.");
        return;
    } finally {
        atlas_ativo = false;
        processando = false;
    }


    iniciarEscuta();
}

reconhecimento.onerror = (event) => {
    console.error("Erro no reconhecimento:", event.error);
};

reconhecimento.onend = () => {
    console.log("Reconhecimento encerrado.");
};

iniciarEscuta();
