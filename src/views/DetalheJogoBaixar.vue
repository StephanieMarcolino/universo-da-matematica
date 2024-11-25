<template>
  <div class="detalhe-jogo">
    <h2>{{ jogo.nome }}</h2>
    <img :src="jogo.imagem" :alt="jogo.nome" class="imagem-detalhe-jogo" />
    <p class="descricao-jogo">{{ jogo.detalhes }}</p>
    <a :href="`/jogo${jogo.id}.pdf`" :download="`jogo${jogo.id}.pdf`" class="button-download">Baixar PDF do Jogo</a>
    <button @click="this.$router.push({ name: 'imprimir-jogos' });">Voltar</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      jogo: {},
    };
  },
  created() {
    const idJogo = this.$route.params.id;
    this.jogo = {
      id: idJogo,
      nome: `Múltiplos e divisores`,
      imagem: require(`../assets/jogo${idJogo}.png`),
      detalhes:
        "Os alunos devem se organizar em duplas. Cada dupla irá receber um tabuleiro, um dado, dois peões e quinze cartas. Ao lançar o dado ele indica quantas casas devem ser percorridas no tabuleiro. Se o estudante parar na casa vermelha, ele deve voltar duas casas. Ao parar na casa azul, ele deve responder uma pergunta das cartas (o colega deve perguntar e conferir a resposta), se acertar ele deve avançar uma casa, se errar ele deve voltar uma casa. Ganha aquele que chegar primeiro ao FIM!",
    };
  },
};
</script>

<style scoped>
.detalhe-jogo {
  max-width: 600px;
  margin: 0 auto;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 0;
}

h2 {
  text-align: center;
  font-size: 2rem;
  color: #333;
  margin-bottom: 20px;
}

.imagem-detalhe-jogo {
  width: 250px;
  height: auto;
  border-radius: 10px;
  margin-bottom: 20px;
  display: block;
}

.descricao-jogo {
  font-size: 0.9rem; /* Texto de descrição menor */
  color: #555;
  line-height: 1.4;
  text-align: justify;
  padding: 0 10px;
}

.button-download {
  width: 50%;
  padding: 10px 20px;
  background-color: #000064;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  display: block;
  text-decoration: none;
  text-align: center;
}

.button-download:hover {
  background-color: #0056b3;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #000064;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

button:hover {
  background-color: #0056b3;
}
</style>
