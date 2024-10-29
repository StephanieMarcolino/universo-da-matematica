<template>
  <div class="detalhes-turma">
    <LoadSpinner :isLoading="loadingSubmit" />
    <h2>Alunos da Turma {{ turma.nome }}</h2>
    <table class="alunos-table" v-if="!loadingSubmit">
      <thead>
        <tr>
          <th>Nome</th>
          <th>Progresso</th>
          <th>Pontuação</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="aluno in alunos" :key="aluno.id">
          <td>{{ aluno.nome }}</td>
          <td>{{ (parseInt(aluno.progresso) - 1) * 10 }}%</td>
          <td>{{ aluno.pontuacao }}</td>
        </tr>
      </tbody>
    </table>
    <p v-if="loadingSubmit">Carregando alunos...</p>
    <button @click="voltar" :disabled="loadingSubmit">Voltar</button>
  </div>
</template>

<script>
import LoadSpinner from '../components/LoadSpiner.vue';

export default {
  components: {
    LoadSpinner
  },
  name: 'DetalhesTurmaComponent',
  data() {
    return {
      turma: {},
      alunos: [],
      loadingSubmit: false,
    };
  },
  created() {
    const turmaId = this.$route.params.turmaId;
    this.getAlunos(turmaId);
  },
  methods: {
    async getAlunos(id) {
      this.loadingSubmit = true; // Ativa o loading
      try {
        const response = await fetch(`http://127.0.0.1:8000/turmas/${id}/alunos/`);
        const data = await response.json();

        // Ordena os alunos pela pontuação (do maior para o menor)
        this.alunos = data.sort((a, b) => b.pontuacao - a.pontuacao);
      } catch (error) {
        console.error('Erro ao buscar as perguntas da API:', error);
      } finally {
        this.loadingSubmit = false; // Desativa o loading
      }
    },
    voltar() {
      this.$router.push({ name: 'VisualizarTurmas' });
    },
  },
};
</script>

<style scoped>
.detalhes-turma {
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