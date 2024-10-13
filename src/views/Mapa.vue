<template>
  <div class="vh-100 vw-100 background">
    <audio ref="backgroundMusic" :src="music" loop></audio>
    <div class="score">
      Pontuação: {{ score }}
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
        <g v-for="level in levels" :key="level.id">
          <foreignObject :x="level.x - 25" :y="level.y - 25" width="55" height="105">
            <button type="button" :class="getLevelClass(level.id)"
              @click="isClickable(level.id) ? selectLevel(level.id) : null" >
              {{ level.id }}
            </button>
          </foreignObject>
        </g>
      </svg>
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
  name: 'LevelMap',
  data() {
    return {
      music: backgroundMusic,
      score: 100,
      currentLevel: 5,
      completedLevels: [1,2,3,4],
      levels: [
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
    };
  },
  methods: {
    async fetchProgress() {
      try {
        const response = await fetch(`http://127.0.0.1:5000/alunos/${1}/progresso`);
        const data = await response.json();
        console.log(data);
        // this.currentLevel = data.progresso;
        // this.completedLevels = Array.from({ length: this.currentLevel }, (_, i) => i + 1);
      } catch (error) {
        console.error('Erro ao buscar progresso:', error);
      }
    },
    selectLevel(levelId) {
      localStorage.setItem('nivelSelecionado', levelId);
      localStorage.setItem('musica', this.isMusicPlaying);
      this.$router.push(`/pergunta/${levelId}`);
    },
    isClickable(levelId) {
      return this.completedLevels.includes(levelId) || levelId === this.currentLevel;
    },
    onMouseDown(e) {
      this.isDragging = true;
      this.startX = e.pageX - this.$refs.levelMap.offsetLeft;
      this.scrollLeft = this.$refs.levelMap.scrollLeft;
      this.$refs.levelMap.style.cursor = 'grabbing';
    },
    onMouseMove(e) {
      if (!this.isDragging) return;
      e.preventDefault();
      const x = e.pageX - this.$refs.levelMap.offsetLeft;
      const walk = (x - this.startX) * 1.5;
      this.$refs.levelMap.scrollLeft = this.scrollLeft - walk;
    },
    onMouseUp() {
      this.isDragging = false;
      this.$refs.levelMap.style.cursor = 'grab';
    },
    onMouseLeave() {
      this.isDragging = false;
      this.$refs.levelMap.style.cursor = 'grab';
    },
    getLevelClass(levelId) {
      if (levelId === this.currentLevel) {
        return 'btn btn-primary level-button rounded-circle';
      } else if (this.completedLevels.includes(levelId)) {
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
  /* Botão estará atrás da imagem */
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
</style>
