<template>
    <div class="visualizar-jogos">
      <LoadSpinner :isLoading="loadingSubmit" />
      <h2>Lista de jogos</h2>
      <button @click="this.$router.push({ name: 'CadastrarJogo' })" :disabled="loadingSubmit">Cadastrar Jogo</button>
      <table class="jogos-table">
        <thead>
          <tr>
            <th>Nome da jogo</th>
            <th>Conteúdo</th>
            <th>Pin</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="jogo in jogos" :key="jogo.id" @click="selecionarjogo(jogo)">
            <td>{{ jogo.titulo }}</td>
            <td>{{ jogo.categoria }}</td>
            <td>{{ jogo.pin }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import LoadSpinner from '../components/LoadSpiner.vue';
  
  export default {
      components: {
      LoadSpinner
    },
    name: 'VisualizarjogosComponent',
    data() {
      return {
        jogos: [],
        loadingSubmit: false,
      };
    },
    mounted() {
      this.buscarjogos();
    },
    methods: {
  
      async buscarjogos() {
        this.loadingSubmit = true;
        try {
          // Chama a API para buscar as jogos
          const response = await fetch(`http://127.0.0.1:8000/jogos/vizualizar/`);
          const data = await response.json();
          this.jogos = data;
  
        } catch (error) {
          console.error('Erro ao buscar as perguntas da API:', error);
        } finally {
          this.loadingSubmit = false; 
        }
      },
  
      selecionarjogo(jogo) {
        this.$router.push({ name: 'DetalhesJogo', params: { jogoId: jogo.id } });
      },
    },
  };
  </script>
  
  <style scoped>
  .visualizar-jogos {
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
  