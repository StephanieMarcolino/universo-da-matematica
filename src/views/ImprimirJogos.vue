<template>
    <div class="games-list">
      <h2>Jogos Disponíveis</h2>
      <div class="games-container">
        <div v-for="game in games" :key="game.id" class="game-card" @click="goToGameDetail(game.id)">
          <img :src="game.image" :alt="game.name" class="game-image" />
          <h3 class="game-title">{{ game.name }}</h3>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'GamesListComponent',
    data() {
      return {
        games: [
      { id: 1, name: 'Trilha dos Múltiplos e Divisores', image: require('../assets/jogo1.png') },
    ],
      };
    },
    methods: {
      goToGameDetail(gameId) {
        this.$router.push(`/imprimir-jogos/jogo/${gameId}`);
      },
    },
  };
  </script>
  
  <style scoped>
  .games-list {
    text-align: center;
  }
  
  .games-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .game-card {
    background-color: #1b1b2a;
    border: 1px solid #ccc;
    border-radius: 8px;
    margin: 10px;
    padding: 10px;
    width: 150px;
    cursor: pointer;
    transition: transform 0.2s;
  }
  
  .game-card:hover {
    transform: scale(1.05);
  }
  
  .game-image {
    width: 100%;
    height: auto;
    border-radius: 5px;
  }
  
  .game-title {
    color: #ffffff;
    margin-top: 10px;
  }
  </style>
  