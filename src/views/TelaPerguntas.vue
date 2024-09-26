<template>
    <div v-if="perguntaAtual" class="vh-100 vw-100 background">
        <div class="vidas">
            <div :class="{ 'coracao-cheio': vidas >= 1, 'coracao-vazio': vidas < 1 }"></div>
            <div :class="{ 'coracao-cheio': vidas >= 2, 'coracao-vazio': vidas < 2 }"></div>
            <div :class="{ 'coracao-cheio': vidas >= 3, 'coracao-vazio': vidas < 3 }"></div>
        </div>

        <div class="card">
            <h2>{{ perguntaAtual.id }}. {{ perguntaAtual.pergunta }}</h2>
            <hr />
            <div class="card-alternativa" v-for="(alternativa, index) in alternativasEmbaralhadas" :key="index" @click="responder(index)">
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
    </div>
</template>


<script>
import perguntasJson from '@/assets/perguntas.json'; // Importa o arquivo JSON

export default {
    data() {
        return {
            perguntas: perguntasJson.perguntas, 
            perguntaAtual: null,
            alternativasEmbaralhadas: [],
            respostaSelecionada: null,
            vidas: 3,
            mensagem: '',
            exibirPopup: false,
            redirecionarParaMapa: false
        };
    },
    mounted() {
        const levelId = localStorage.getItem('nivelSelecionado');
        if (levelId && parseInt(levelId) > 0 && parseInt(levelId) <= this.perguntas.length) {
            console.log(`Nível ${levelId} selecionado!`);
            this.selecionarPergunta(parseInt(levelId));
        } else {
            console.error(`ID de nível inválido: ${levelId}`);
            // Lógica para tratar quando o ID do nível não é válido
        }
    },
    methods: {
        selecionarPergunta(levelId) {
            // Encontrar a pergunta pelo ID
            this.perguntaAtual = this.perguntas.find(pergunta => pergunta.id === levelId);

            // Embaralhar as alternativas
            this.embaralharAlternativas();
        },
        embaralharAlternativas() {
            // Copiar e embaralhar as alternativas
            const alternativas = [
                { texto: this.perguntaAtual.resposta, correta: true },
                { texto: this.perguntaAtual.alternativa1, correta: false },
                { texto: this.perguntaAtual.alternativa2, correta: false },
                { texto: this.perguntaAtual.alternativa3, correta: false }
            ];

            // Embaralhar o array de alternativas
            this.alternativasEmbaralhadas = this.shuffleArray(alternativas);
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
                    if (this.vidas === 3) {
                        this.mensagem = 'Incrível! Você acertou de primeira, excelente trabalho!';
                    } else if (this.vidas === 2) {
                        this.mensagem = 'Boa! Acertou na segunda tentativa, continue assim!';
                    } else if (this.vidas === 1) {
                        this.mensagem = 'Ufa! Você acertou no último momento, parabéns pela persistência!';
                    }
                } else {
                    this.vidas--;
                    this.redirecionarParaMapa = false;
                    if (this.vidas > 0) {
                        if (this.vidas === 2) {
                            this.mensagem = 'Não desista! Ainda tem mais duas chances!';
                        } else if (this.vidas === 1) {
                            this.mensagem = 'Última tentativa! Pense com cuidado!';
                        }
                    } else {
                        this.mensagem = 'Você perdeu todas as vidas. Não desanime, tente novamente!';
                    }
                }
                this.exibirPopup = true; 
            } else {
                this.mensagem = 'Por favor, selecione uma resposta!';
                this.exibirPopup = true; // Exibe o popup
            }
        },
        fecharPopup() {
            this.exibirPopup = false; 
            if (this.redirecionarParaMapa) {
                // Se a resposta foi correta, redireciona para o mapa
                this.$router.push(`/mapa`);
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
    position: relative; /* Adiciona posição relativa para a mensagem */
}

.card-alternativa {
    display: flex;
    flex-direction: row;
    align-items: center;
    max-width: 400px;
    width: 80%;
    height: 50px; /* Altura reduzida */
    border: 1px solid grey;
    color: grey;
    border-radius: 5px;
    padding: 5px; /* Reduzir o padding */
    margin-bottom: 5px;
}

.card-alternativa:hover {
    background-color: rgba(0, 123, 255, 0.1); /* Efeito de destaque ao passar o mouse */
}

.radio-button {
    margin-left: auto;
    width: 20px; /* Largura do botão de rádio */
    height: 20px; /* Altura do botão de rádio */
    appearance: none; /* Remove o estilo padrão */
    background-color: white; /* Cor de fundo do botão de rádio */
    border: 2px solid grey; /* Borda do botão de rádio */
    border-radius: 50%; /* Forma circular */
    position: relative;
    cursor: pointer;
}

.radio-button:checked {
    background-color: white; /* Fundo branco quando selecionado */
    border-color: blue; /* Borda azul quando selecionado */
}

.radio-button:checked::after {
    content: '';
    position: absolute;
    top: 50%; /* Centraliza verticalmente */
    left: 50%; /* Centraliza horizontalmente */
    width: 10px; /* Tamanho do círculo interno */
    height: 10px; /* Tamanho do círculo interno */
    background-color: blue; /* Cor do círculo interno */
    border-radius: 50%; /* Forma circular */
    transform: translate(-50%, -50%); /* Centraliza o círculo interno */
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
    background-color: red; /* Cor do coração cheio */
    margin-right: 5px;
    mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" width="48px" height="48px"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>');
    mask-size: cover;
    -webkit-mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" width="48px" height="48px"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>');
    mask-size: cover;
}

.coracao-vazio {
    width: 30px;
    height: 30px;
    background-color: lightgrey; /* Cor do coração vazio */
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
    max-width: 400px; /* Define o tamanho máximo do popup */
    width: 90%; /* Ajusta a largura para caber bem em diferentes tamanhos de tela */
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
    width: 100px; /* Tamanho ajustável */
    height: 100px;
}


</style>
  