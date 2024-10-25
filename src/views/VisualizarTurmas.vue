<template>
  <div class="visualizar-turmas">
    <h2>Lista de Turmas</h2>
    <table class="turmas-table">
      <thead>
        <tr>
          <th>Nome da Turma</th>
          <th>Escola</th>
          <th>Série</th>
          <th>Ano</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="turma in turmas" :key="turma.id" @click="selecionarTurma(turma)">
          <td>{{ turma.nome }}</td>
          <td>{{ turma.escola }}</td>
          <td>{{ turma.serie }}° série</td>
          <td>{{ turma.ano }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'VisualizarTurmasComponent',
  data() {
    return {
      turmas: [],
    };
  },
  mounted() {
    this.buscarTurmas();
  },
  methods: {

    async buscarTurmas() {
      try {
        // Chama a API para buscar as turmas
        const response = await fetch(`http://127.0.0.1:8000/turmas/vizualizar/`);
        const data = await response.json();
        this.turmas = data;

      } catch (error) {
        console.error('Erro ao buscar as perguntas da API:', error);
      }
    },

    selecionarTurma(turma) {
      this.$router.push({ name: 'DetalhesTurma', params: { turmaId: turma.id } });
    },
  },
};
</script>

<style scoped>
.visualizar-turmas {
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

tbody tr {
  cursor: pointer;
}

tbody tr:hover {
  background-color: #f0f0f0;
  /* Efeito de hover mais claro */
}

tbody tr:last-child td {
  border-bottom: none;
}
</style>
