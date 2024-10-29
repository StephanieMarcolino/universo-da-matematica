<template>
  <div class="vh-100 vw-100 background">
    <LoadSpinner :isLoading="loadingSubmit" />
    <audio ref="backgroundMusic" :src="musica" loop></audio>
    <div class="score">
      Pontuação: {{ pontuacao }}
    </div>

    <div class="level-map" ref="levelMap">
      <svg class="vh-100" ref="svgMap">
        <!-- Caminho Pontilhado -->
        <path d="M 0 150 
             T 50 200
             T 200 250
             T 350 400
             Q 400 200, 500 225
             T 650 350
             T 800 225
             Q 900 300, 900 350
             T 900 400
             T 1050 250
             T 1200 350
             T 1300 225" stroke="white" stroke-dasharray="5,5" stroke-width="3" fill="transparent" />

        <!-- Botões dos Níveis -->
        <g v-for="level in niveis" :key="level.id">
          <foreignObject :x="level.x - 25" :y="level.y - 25" width="55" height="105">
            <button type="button" :class="getLevelClass(level.id)"
              @click="isClickable(level.id) ? selectLevel(level.id) : null" >
              {{ level.id }}
            </button>
          </foreignObject>
        </g>
      </svg>
    </div>

    <!-- Mensagem de parabéns quando o nível 10 for concluído -->
    <div v-if="nivelConcluido" class="congratulations-popup">
      <h2>Parabéns!</h2>
      <p>Você concluiu todos os níveis!</p>
      <p>Sua pontuação final é: {{ pontuacao }}</p>
      <button @click="fecharPopup">Fechar</button>
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
import LoadSpinner from '../components/LoadSpiner.vue';

export default {
    components: {
    LoadSpinner,
  },
  name: 'LevelMap',
  data() {
    return {
      musica: backgroundMusic,
      loadingSubmit: false,
      pontuacao: 0,
      nivelAtual: 1,
      niveisCompletos: [],
      nivelConcluido: false,
      niveis: [
        { id: 1, x: 50, y: 200 },
        { id: 2, x: 200, y: 250 },
        { id: 3, x: 350, y: 400 },
        { id: 4, x: 500, y: 225 },
        { id: 5, x: 650, y: 350 },
        { id: 6, x: 800, y: 225 },
        { id: 7, x: 900, y: 400 },
        { id: 8, x: 1050, y: 250 },
        { id: 9, x: 1200, y: 350 },
        { id: 10, x: 1300, y: 225 },
      ],
      volume: 0.5,
      isMenuOpen: false,
      isMusicPlaying: true,
      isDragging: false,
      startX: 0,
      scrollLeft: 0,
      jogo: localStorage.getItem("jogoId"),
      perguntas: [],
      alunoId: localStorage.getItem("aluno"),
    };
  },
  methods: {
    async buscarPerguntas() {
      this.loadingSubmit = true;
      try {
        const response = await fetch(`http://127.0.0.1:8000/jogo/${this.jogo}/questoes/`);
        const data = await response.json();
        this.perguntas = data;
      } catch (error) {
        console.error('Erro ao buscar as perguntas da API:', error);
      } finally {
        this.loadingSubmit = false;
      }
    },
    async fetchProgress() {
      this.loadingSubmit = true;
      try {
        const response = await fetch(`http://127.0.0.1:8000/alunos/${this.alunoId}/`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const data = await response.json();
        this.nivelAtual = data.progresso;
        this.niveisCompletos = Array.from({ length: this.nivelAtual }, (_, i) => i + 1);
        this.pontuacao = data.pontuacao;
        if (this.nivelAtual === 11) {
          this.nivelConcluido = true;
        }
        localStorage.setItem('pontuacao', this.pontuacao);
      } catch (error) {
        console.error('Erro ao buscar progresso:', error);
      } finally {
        this.loadingSubmit = false;
      }
    },
    selectLevel(levelId) {
      this.loadingSubmit = true;
      localStorage.setItem('nivelSelecionado', levelId);
      localStorage.setItem('musica', this.isMusicPlaying);
      this.$router.push({
        name: 'pergunta',
        params: { id: levelId },
        query: { pergunta: JSON.stringify(this.perguntas[levelId - 1]) }
      }).finally(() => {
        this.loadingSubmit = false;
      });
    },
    isClickable(levelId) {
      return levelId === this.nivelAtual;
    },
    getLevelClass(levelId) {
      if (levelId === this.nivelAtual) {
        return 'btn btn-primary level-button rounded-circle';
      } else if (this.niveisCompletos.includes(levelId)) {
        return 'btn btn-light level-button rounded-circle text-primary';
      } else {
        return 'btn btn-secondary level-button rounded-circle';
      }
    },
    adjustVolume() {
      const audio = this.$refs.backgroundMusic;
      audio.volume = this.volume;
    },
    toggleMusic() {
      const audio = this.$refs.backgroundMusic;
      if (this.isMusicPlaying) {
        audio.play();
      } else {
        audio.pause();
      }
      localStorage.setItem('musica', this.isMusicPlaying);
    },
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    fecharPopup() {
      this.nivelConcluido = false;
    }
  },
  async mounted() {
    const storedMusicState = localStorage.getItem('musica');
    this.isMusicPlaying = storedMusicState === 'true';

    const audio = this.$refs.backgroundMusic;
    audio.volume = this.volume;

    if (this.isMusicPlaying) {
      audio.play();
    } else {
      audio.pause();
    }

    await this.fetchProgress();
    this.buscarPerguntas();

    const levelMap = this.$refs.levelMap;
    levelMap.addEventListener('mousedown', this.onMouseDown);
    levelMap.addEventListener('mousemove', this.onMouseMove);
    levelMap.addEventListener('mouseup', this.onMouseUp);
    levelMap.addEventListener('mouseleave', this.onMouseLeave);
  },
  beforeUnmount() {
    const levelMap = this.$refs.levelMap;
    levelMap.removeEventListener('mousedown', this.onMouseDown);
    levelMap.removeEventListener('mousemove', this.onMouseMove);
    levelMap.removeEventListener('mouseup', this.onMouseUp);
    levelMap.removeEventListener('mouseleave', this.onMouseLeave);
  },
};
</script>

<style scoped>
.background {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url('../assets/fundo1.png');
  background-size: cover;
  background-position: center;
  overflow: hidden;
}

.btn-secondary {
  background-color: #6c757d;
  /* Cinza normal e opaco */
  color: white;
  /* Cor do texto em branco */
  pointer-events: none;
  /* Impede interação com os botões inativos */
  opacity: 1;
  /* Garante que o botão não seja transparente */
}


.level-map {
  display: flex;
  justify-content: flex-start;
  /* Alinha os elementos à esquerda */
  align-items: center;
  cursor: grab;
  overflow-x: auto;
  /* Permite rolagem horizontal */
  white-space: nowrap;
  width: 100%;
  /* Largura total do contêiner */
}

.level-map:active {
  cursor: grabbing;
}

svg {
  width: auto;
  /* Ajuste automático da largura do SVG */
  height: 100%;
  /* Altura fixa para o SVG */
  min-width: 1400px;
  /* Garantir que a largura mínima do SVG seja suficiente */
}

.score {
  position: absolute;
  top: 20px;
  left: 20px;
  color: white;
  font-size: 1.5rem;
  font-weight: bold;
  z-index: 10;
}

.level-button {
  position: relative;
  z-index: 0;
  width: 50px;
  height: 50px;
  font-size: 1.2rem;
  border-radius: 50%;
  font-weight: bold;
}

.level-button:hover {
  background-color: white;
  border-color: #0097fc;
  color: #051a77;
  font-weight: bold;
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
.congratulations-popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: rgba(0, 0, 0, 0.8);
  padding: 20px;
  border-radius: 10px;
  color: white;
  text-align: center;
  z-index: 1000;
}

.congratulations-popup h2 {
  margin-bottom: 10px;
}

.congratulations-popup button {
  margin-top: 10px;
  padding: 10px;
  background-color: #000064;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

</style>
