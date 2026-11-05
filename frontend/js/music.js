let player = null;


export function tocarMusica(dados){
    console.log("MUSIC.JS ESTÁ SENDO EXECUTADO!");

    const musicaId = dados.musica_id.video_id

    if (!musicaId) {
        throw new Error("ID da música não foi fornecido ou é inválido.");
    }

    if (!player) {
        throw new Error("player inexistente")

    }

    console.log('FINAL');
   player.loadVideoById(musicaId);
}

function onYouTubeIframeAPIReady() {
    if (player) return;

    player = new YT.Player("youtube-player", {
        playerVars: {
            origin: window.location.origin
        },
        events: {
            onError: (event) => {
                console.error("Erro do YouTube:", event.data);
            }
        }
    });
    }

        window.onYouTubeIframeAPIReady = onYouTubeIframeAPIReady;

        if (window.YT && window.YT.Player) {
            onYouTubeIframeAPIReady();
    }