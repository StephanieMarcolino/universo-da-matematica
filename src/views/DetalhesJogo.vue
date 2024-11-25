<template>
  <div class="detalhes-jogo">
    <LoadSpinner :isLoading="loadingSubmit" />
    <h2>Perguntas do Jogo {{ jogo.nome }}</h2>
    <table class="perguntas-table" v-if="!loadingSubmit">
      <thead>
        <tr>
          <th>Descrição</th>
          <th>Complexidade</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="pergunta in perguntas" :key="pergunta.id">
          <td>{{ pergunta.descricao }}</td>
          <td>{{ pergunta.classificacao}}</td>
        </tr>
      </tbody>
    </table>
    <p v-if="loadingSubmit">Carregando perguntas...</p>
    <button @click="voltar" :disabled="loadingSubmit">Voltar</button>
  </div>
</template>

<script>
import LoadSpinner from '../components/LoadSpiner.vue';

export default {
  components: {
    LoadSpinner
  },
  name: 'DetalhesjogoComponent',
  data() {
    return {
      jogo: {},
      perguntas: [],
      loadingSubmit: false,
    };
  },
  created() {
    const jogoId = this.$route.params.jogoId;
    this.getperguntas(jogoId);
  },
  methods: {
    async getperguntas(id) {
      this.loadingSubmit = true; // Ativa o loading
      try {
        const response = await fetch(`http://127.0.0.1:8000/jogo/${id}/questoes/`);
        const data = await response.json();

        this.perguntas = data;
      } catch (error) {
        console.error('Erro ao buscar as perguntas da API:', error);
      } finally {
        this.loadingSubmit = false; // Desativa o loading
      }
    },
    voltar() {
      this.$router.push({ name: 'VisualizarJogos' });
    },
  },
};
</script>

<style scoped>
.detalhes-jogo {
  max-width: 800px;
  margin: 20px auto;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
  /* Cor mais suave para o título */
}

table {
  width: 100%;
  border-collapse: collapse;
  border-radius: 10px;
  overflow: hidden;
  background-color: #f9f9f9;
  /* Fundo claro para a tabela */
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  /* Leve sombra para destaque */
}

th,
td {
  padding: 12px;
  border: 1px solid #ddd;
  text-align: center;
  color: #333;
  /* Texto mais escuro para contraste */
}

thead {
  background-color: #b3b3b3;
  /* Fundo azul para o cabeçalho */
  color: #ffffff;
  /* Texto branco no cabeçalho */
}

tbody tr:last-child td {
  border-bottom: none;
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