console.log("Atlas JS conectado");

const reconhecimento = new webkitSpeechRecognition();

reconhecimento.lang = "pt-BR";
reconhecimento.continuous = true;
reconhecimento.interimResults = true;

let atlas_ativo = false;

function escutar() {


    reconhecimento.onstart = function () {
        console.log("COMEÇOU A ESCUTAR");
    };

    reconhecimento.onresult = function (event) {
        console.log("RESULTADO");

        indice = event.resultIndex;

        if (event.results[indice].isFinal) {

            const texto_comando = event.results[indice][0].transcript;
            let texto = texto_comando.toLowerCase().trim();

            if (texto  === 'atlas') {
                reconhecimento.stop()

                atlas_ativo = true;

                const fala = new SpeechSynthesisUtterance("Pode falar");

                fala.onend = function () {
                    escutar();
                };

                speechSynthesis.speak(fala);

            }
            else if (texto.startsWith('atlas')) {

                const comando = texto
                console.log(comando);

            }

            else{
                if (atlas_ativo) {
                    const comando = texto
                    console.log(comando);
                    atlas_ativo = false;
                }
            }
        }
    };


    reconhecimento.onerror = function (event) {
        console.log("ERRO:", event.error);
    };

    reconhecimento.onend = function () {
        console.log("TERMINOU");
    };

    reconhecimento.start();
    }

escutar();
