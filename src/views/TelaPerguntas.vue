<template>
    <div v-if="perguntaAtual" class="vh-100 vw-100 background">
        <audio ref="backgroundMusic" :src="music" loop></audio>
        <div class="vidas">
            <div :class="{ 'coracao-cheio': vidas >= 1, 'coracao-vazio': vidas < 1 }"></div>
            <div :class="{ 'coracao-cheio': vidas >= 2, 'coracao-vazio': vidas < 2 }"></div>
            <div :class="{ 'coracao-cheio': vidas >= 3, 'coracao-vazio': vidas < 3 }"></div>
        </div>

        <div class="card">
            <h2>{{ perguntaAtual.id }}. {{ perguntaAtual.descricao }}</h2>
            <hr />
            <div class="card-alternativa" v-for="(alternativa, index) in alternativasEmbaralhadas" :key="index"
                @click="responder(index)">
                <h2>{{ index + 1 }}. {{ alternativa.texto }}</h2>
                <input type="radio" :id="'alternativa' + index" name="alternativa" class="radio-button"
                    v-model="respostaSelecionada" :value="index" />
            </div>


            <button type="button" class="btn btn-outline-primary" @click="conferir">Ok</button>
        </div>

        <!-- Popup modal -->
        <div v-if="exibirPopup" class="popup-container">
            <div class="popup-content">
                <!-- Ícone de acordo com a mensagem -->
                <div class="popup-icon">
                    <img v-if="vidas === 3 && redirecionarParaMapa" src="@/assets/meme-3vidas.png" alt="Incrível" />
                    <img v-if="vidas === 2 && !redirecionarParaMapa" src="@/assets/meme-2vidas.png" alt="Bom" />
                    <img v-if="vidas === 1 && !redirecionarParaMapa" src="@/assets/meme-1vida.png" alt="Ufa" />
                    <img v-if="vidas === 0" src="@/assets/meme-0vida.png" alt="Game Over" />
                </div>

                <h2 class="popup-message">{{ mensagem }}</h2>
                <button class="btn btn-primary popup-close" @click="fecharPopup">Fechar</button>
            </div>
        </div>
        <!-- Botão de Menu -->
        <button class="menu-button" @click="toggleMenu">
            ☰
        </button>

        <!-- Popup de Controle de Volume -->
        <div v-if="isMenuOpen" class="popup">
            <h3>Opções</h3>
            <!-- Controle de Volume -->
            <label for="volumeControl">Volume:</label>
            <input id="volumeControl" type="range" min="0" max="1" step="0.1" v-model="volume" @input="adjustVolume" />

            <!-- Ativar/Desativar Música -->
            <div>
                <label>
                    <input type="checkbox" v-model="isMusicPlaying" @change="toggleMusic" />
                    Música Ativada
                </label>
            </div>

            <!-- Fechar Popup -->
            <button @click="toggleMenu">Fechar</button>
        </div>
    </div>
</template>

<script>
import backgroundMusic from '@/assets/audio-fundo.mp3';

export default {
    data() {
        return {
            perguntaAtual: null,
            alternativasEmbaralhadas: [],
            respostaSelecionada: null,
            vidas: 3,
            mensagem: '',
            exibirPopup: false,
            redirecionarParaMapa: false,
            music: backgroundMusic,
            volume: 0.5,
            isMenuOpen: false,
            isMusicPlaying: true,
            isDragging: false,
            errosConsecutivos: 0,
            alunoId: localStorage.getItem("aluno"),
            levelId: localStorage.getItem('nivelSelecionado'),
            pontuacaoAntiga: localStorage.getItem('pontuacao'),
            pontuacao: ''
        };
    },
    mounted() {
        this.perguntaAtual = JSON.parse(this.$route.query.pergunta);

        const storedMusicState = localStorage.getItem('musica');
        this.isMusicPlaying = storedMusicState === 'true';

        const storedErrosConsecutivos = localStorage.getItem('errosConsecutivos');
        this.errosConsecutivos = storedErrosConsecutivos ? parseInt(storedErrosConsecutivos) : 0;

        const audio = this.$refs.backgroundMusic;
        if (audio) {
            audio.volume = this.volume;
            setTimeout(() => {
                if (this.isMusicPlaying) {
                    audio.play().catch((error) => {
                        console.warn("O navegador bloqueou a reprodução automática. O usuário precisará ativar manualmente." + error);
                    });
                } else {
                    audio.pause();
                }
            }, 100);
        }

        this.embaralharAlternativas();
    },
    methods: {

        embaralharAlternativas() {
            const alternativas = [
                { texto: this.perguntaAtual.resposta, correta: true },
                { texto: this.perguntaAtual.alternativa1, correta: false },
                { texto: this.perguntaAtual.alternativa2, correta: false },
                { texto: this.perguntaAtual.alternativa3, correta: false }
            ];

            // Embaralhar o array de alternativas
            this.alternativasEmbaralhadas = this.shuffleArray(alternativas);
            // Verifica se deve remover 2 alternativas erradas
            if (this.errosConsecutivos >= 2) {
                this.removerAlternativasErradas();
                // Exibe uma mensagem informando que o jogador ganhou uma ajuda
                this.mensagem = 'Como você errou duas vezes seguidas, duas alternativas foram removidas para facilitar sua próxima tentativa!';
                this.exibirPopup = true; // Exibe o popup com a mensagem
            }
        },
        removerAlternativasErradas() {
            // Filtra as alternativas para manter a correta e mais uma incorreta
            const alternativasErradas = this.alternativasEmbaralhadas.filter(alt => !alt.correta);
            const alternativaCorreta = this.alternativasEmbaralhadas.find(alt => alt.correta);

            // Escolhe aleatoriamente uma alternativa incorreta para manter
            const alternativaExtra = alternativasErradas[Math.floor(Math.random() * alternativasErradas.length)];
            this.alternativasEmbaralhadas = this.shuffleArray([alternativaCorreta, alternativaExtra]);

            // Reseta o contador de erros consecutivos para 0
            this.errosConsecutivos = 0;
            localStorage.setItem('errosConsecutivos', this.errosConsecutivos);
        },
        shuffleArray(array) {
            // Função para embaralhar um array (Fisher-Yates shuffle)
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
            return array;
        },
        responder(index) {
            this.respostaSelecionada = index; // Define a resposta selecionada ao clicar na alternativa
        },
        conferir() {
            if (this.respostaSelecionada !== null) {
                const respostaCorreta = this.alternativasEmbaralhadas.find(alternativa => alternativa.correta);
                const respostaUsuario = this.alternativasEmbaralhadas[this.respostaSelecionada];
                if (respostaCorreta.texto === respostaUsuario.texto) {
                    this.redirecionarParaMapa = true;
                    this.mensagem = this.vidas === 3
                        ? 'Incrível! Você acertou de primeira, excelente trabalho!'
                        : this.vidas === 2
                            ? 'Boa! Acertou na segunda tentativa, continue assim!'
                            : 'Ufa! Você acertou no último momento, parabéns pela persistência!';
                    this.errosConsecutivos = 0; // Reseta os erros consecutivos
                    localStorage.setItem('errosConsecutivos', this.errosConsecutivos);
                } else {
                    this.vidas--;
                    this.redirecionarParaMapa = false;

                    if (this.vidas > 0) {
                        this.mensagem = this.vidas === 2
                            ? 'Não desista! Ainda tem mais duas chances!'
                            : 'Última tentativa! Pense com cuidado!';
                    } else {
                        this.errosConsecutivos++;
                        this.mensagem = 'Você perdeu todas as vidas. Não desanime, tente novamente!';
                        this.redirecionarParaMapa = true;
                    }
                }
                this.exibirPopup = true;
            } else {
                this.mensagem = 'Por favor, selecione uma resposta!';
                this.exibirPopup = true; // Exibe o popup
            }
        },

        async atualizarNivel() {
            try {
                const response = await fetch(`http://127.0.0.1:8000/alunos/${this.alunoId}/`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ pontuacao: this.pontuacao, progresso: parseInt(this.levelId) + 1 }), // Enviando o progresso
                });


                if (!response.ok) {
                    const errorData = await response.json(); // Captura os dados de erro da resposta
                    throw new Error(`Erro ${response.status}: ${JSON.stringify(errorData)}`);

                }

                const data = await response.json();
                console.log('Nível atualizado:', data);
            } catch (error) {
                console.error('Erro ao atualizar nível do aluno:', error);
            }
        },

        adjustVolume() {
            const audio = this.$refs.backgroundMusic;
            if (audio) {
                audio.volume = this.volume;
            }
        },
        toggleMusic() {
            const audio = this.$refs.backgroundMusic;
            if (audio) {
                if (this.isMusicPlaying) {
                    audio.play();
                } else {
                    audio.pause();
                }
                localStorage.setItem('musica', this.isMusicPlaying);
            }
        },
        toggleMenu() {
            this.isMenuOpen = !this.isMenuOpen;
        },

        fecharPopup() {
            this.exibirPopup = false;
            localStorage.setItem('musica', this.isMusicPlaying);
            if (this.redirecionarParaMapa) {
                localStorage.setItem('errosConsecutivos', this.errosConsecutivos);
                console.log("erros",this.errosConsecutivos)
                // Atualiza o nível do aluno antes de redirecionar
                this.pontuacao = this.vidas === 3
                    ? parseInt(this.pontuacaoAntiga, 10) + 30
                    : this.vidas === 2
                        ? parseInt(this.pontuacaoAntiga, 10) + 20
                        : this.vidas === 1
                            ? parseInt(this.pontuacaoAntiga, 10) + 10
                            : parseInt(this.pontuacaoAntiga, 10) + 0;
                this.atualizarNivel()
                    .then(() => {
                        // Redireciona para o mapa após a atualização
                        this.$router.push(`/mapa`);
                    })
                    .catch((error) => {
                        console.error('Erro ao redirecionar para o mapa:', error);
                    });
            }
        }

    }
};
</script>

<style scoped>
.background {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-image: url('../assets/fundo.jpg');
    background-size: cover;
    background-position: center;
}

.card {
    display: flex;
    border-radius: 5px;
    flex-direction: column;
    align-items: center;
    max-width: 600px;
    width: 60%;
    height: auto;
    background-color: rgba(255, 255, 255, 0.8);
    position: relative;
    /* Adiciona posição relativa para a mensagem */
}

.card-alternativa {
    display: flex;
    flex-direction: row;
    align-items: center;
    max-width: 400px;
    width: 80%;
    height: 50px;
    /* Altura reduzida */
    border: 1px solid grey;
    color: grey;
    border-radius: 5px;
    padding: 5px;
    /* Reduzir o padding */
    margin-bottom: 5px;
}

.card-alternativa:hover {
    background-color: rgba(0, 123, 255, 0.2);
    /* Efeito de destaque ao passar o mouse */
}

.card-alternativa:active {
    background-color: rgba(0, 123, 255, 0.5);
    /* Efeito de clique */
}


.radio-button {
    margin-left: auto;
    width: 20px;
    /* Largura do botão de rádio */
    height: 20px;
    /* Altura do botão de rádio */
    appearance: none;
    /* Remove o estilo padrão */
    background-color: white;
    /* Cor de fundo do botão de rádio */
    border: 2px solid grey;
    /* Borda do botão de rádio */
    border-radius: 50%;
    /* Forma circular */
    position: relative;
    cursor: pointer;
}

.radio-button:checked {
    background-color: white;
    /* Fundo branco quando selecionado */
    border-color: blue;
    /* Borda azul quando selecionado */
}

.radio-button:checked::after {
    content: '';
    position: absolute;
    top: 50%;
    /* Centraliza verticalmente */
    left: 50%;
    /* Centraliza horizontalmente */
    width: 10px;
    /* Tamanho do círculo interno */
    height: 10px;
    /* Tamanho do círculo interno */
    background-color: blue;
    /* Cor do círculo interno */
    border-radius: 50%;
    /* Forma circular */
    transform: translate(-50%, -50%);
    /* Centraliza o círculo interno */
}

.btn-outline-primary {
    margin: auto;
    width: 60%;
}

.vidas {
    position: absolute;
    top: 20px;
    right: 20px;
    display: flex;
    flex-direction: row;
}

.coracao-cheio {
    width: 30px;
    height: 30px;
    background-color: red;
    /* Cor do coração cheio */
    margin-right: 5px;
    mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" width="48px" height="48px"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>');
    mask-size: cover;
    -webkit-mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" width="48px" height="48px"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>');
    mask-size: cover;
}

.coracao-vazio {
    width: 30px;
    height: 30px;
    background-color: lightgrey;
    /* Cor do coração vazio */
    margin-right: 5px;
    mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" width="48px" height="48px"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>');
    mask-size: cover;
    -webkit-mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" width="48px" height="48px"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>');
    mask-size: cover;
}

.popup-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

.popup-content {
    background: #2e2e2e;
    color: #fff;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
    max-width: 400px;
    /* Define o tamanho máximo do popup */
    width: 90%;
    /* Ajusta a largura para caber bem em diferentes tamanhos de tela */
}

.popup-message {
    margin-bottom: 20px;
    font-size: 1rem;
}

.popup-close {
    background: linear-gradient(90deg, #1A6DFF, #C822FF);
    border: none;
    color: #fff;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
}

.popup-close:hover {
    opacity: 0.5;
}

.popup-icon {
    display: flex;
    justify-content: center;
    margin-bottom: 15px;
}

.popup-icon img {
    width: 100px;
    /* Tamanho ajustável */
    height: 100px;
}

.menu-button {
    position: absolute;
    bottom: 20px;
    right: 20px;
    background-color: #000064;
    border: none;
    color: white;
    padding: 15px;
    border-radius: 50%;
    font-size: 24px;
    cursor: pointer;
}

.menu-button:hover {
    background-color: #0202aa;
}

.popup {
    position: absolute;
    bottom: 80px;
    right: 20px;
    background-color: rgba(0, 0, 0, 0.5);
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    z-index: 1000;
    color: #fff;
}

.popup h3 {
    margin-top: 0;
}

.popup input[type="range"] {
    width: 100%;
}

.popup button {
    margin-top: 10px;
    padding: 10px;
    background-color: #000064;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
</style>