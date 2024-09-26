<template>
    <div class="detalhes-turma">
      <h2>Alunos da Turma {{ turma.nome }}</h2>
      <table class="alunos-table">
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
            <td>{{ aluno.progresso }}%</td>
            <td>{{ aluno.pontuacao }}</td>
          </tr>
        </tbody>
      </table>
      <button @click="voltar">Voltar</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DetalhesTurmaComponent',
    data() {
      return {
        turma: {},
        alunos: [
          { id: 1, nome: 'Aluno 1', progresso: 80, pontuacao: 95 },
          { id: 2, nome: 'Aluno 2', progresso: 90, pontuacao: 98 },
        ],
      };
    },
    created() {
      const turmaId = this.$route.params.turmaId;
      this.turma = this.getTurmaById(turmaId);
    },
    methods: {
      getTurmaById(id) {
        const turmas = [
          { id: 1, nome: 'Turma A', escola: 'Escola 1', serie: 6, ano: 2024 },
          { id: 2, nome: 'Turma B', escola: 'Escola 2', serie: 7, ano: 2025 },
        ];
        return turmas.find(turma => turma.id === Number(id));
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
    color: #333; /* Cor mais suave para o título */
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    border-radius: 10px;
    overflow: hidden;
    background-color: #f9f9f9; /* Fundo claro para a tabela */
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Leve sombra para destaque */
  }
  
  th, td {
    padding: 12px;
    border: 1px solid #ddd;
    text-align: center;
    color: #333; /* Texto mais escuro para contraste */
  }
  
  thead {
    background-color: #b3b3b3; /* Fundo azul para o cabeçalho */
    color: #ffffff; /* Texto branco no cabeçalho */
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
  