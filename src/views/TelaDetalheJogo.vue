<template>
    <div class="game-detail">
      <h2>{{ game.name }}</h2>
      <img :src="game.image" :alt="game.name" class="game-detail-image" />
      <p>Detalhes do jogo aqui...</p>
      <a href="/jogoTeste.pdf" download="jogoTeste.pdf" class="download-button">Baixar PDF do Jogo</a>
      <router-link to="/imprimir-jogos">Voltar para a lista de jogos</router-link>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        game: {},
      };
    },
    created() {
      const gameId = this.$route.params.id;
      // Aqui você pode buscar os detalhes do jogo usando o gameId
      // Exemplo de dados de um jogo para simulação
      this.game = {
        id: gameId,
        name: `Jogo ${gameId}`,
        image: require(`../assets/jogo${gameId}.jpg`),
      };
    },
  };
  </script>
  
  <style scoped>
  .game-detail {
    text-align: center;
  }
  
  .game-detail-image {
    width: 200px;
    height: auto;
    margin-top: 20px;
  }
  </style>
  