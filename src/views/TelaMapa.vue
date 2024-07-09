<template>
  <div class="vh-100 vw-100 background">
  <div class="vh-100 vw-100 level-map">
    <svg class="vh-100 vw-100">
      <!-- Caminho Pontilhado -->
      <path
        d="M 0 150 
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
           T 1300 225
           "
        stroke="white"
        stroke-dasharray="5,5"
        stroke-width="3"
        fill="transparent"
      />

      <!-- Botões dos Níveis com Bootstrap -->
      <g v-for="level in levels" :key="level.id">
        <foreignObject :x="level.x - 25" :y="level.y - 25" width="55" height="55">
          <div class="d-flex justify-content-center align-items-center rounded-circle">
            <button
              type="button"
              class="btn btn-secondary level-button rounded-circle"
              @click="selectLevel(level.id)"
            >
              {{ level.id }}
            </button>
          </div>
        </foreignObject>
      </g>
    </svg>
  </div>
</div>
</template>

<script>
export default {
  name: 'LevelMap',
  data() {
    return {
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
    };
  },
  methods: {
    selectLevel(levelId) {
      alert(`Nível ${levelId} selecionado!`);
      localStorage.setItem('nivelSelecionado', levelId);
      this.$router.push(`/pergunta/${levelId}`);
    },
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
}

.level-map {
  display: flex;
  justify-content: center;
  align-items: center;
}

.level-button {
  width: 100%;
  height: 100%;
  font-size: 1.2rem;
  border-radius: 1;
  font-weight: bold
}

.level-button:hover{
  background-color: white;
    border-color: #0097fc;
    color: #051a77;
    font-weight: bold
}

.level-text {
  fill: #fff;
  font-weight: bold;
}
</style>
