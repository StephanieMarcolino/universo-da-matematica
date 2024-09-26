<template>
    <div class="cadastro-jogo">
      <h2>Cadastro de Jogo</h2>
      <form @submit.prevent="cadastrarJogo">
        <div class="form-group">
          <label for="nomeJogo">Nome do Jogo</label>
          <input
            type="text"
            id="nomeJogo"
            v-model="nome"
            required
            placeholder="Digite o nome do jogo"
          />
        </div>
        <div class="form-group">
          <label for="serie">Série</label>
          <select id="serie" v-model="filtro.serie" @change="filtrarPerguntas" required>
            <option value="" disabled selected>Selecione a série</option>
            <option value="6">6° série</option>
            <option value="7">7° série</option>
            <option value="8">8° série</option>
            <option value="9">9° série</option>
          </select>
        </div>
        <div class="form-group">
          <label for="conteudo">Conteúdo</label>
          <select id="conteudo" v-model="filtro.conteudo" @change="filtrarPerguntas" required>
            <option value="" disabled selected>Selecione o conteúdo</option>
            <option value="aritmetica">Aritmética</option>
            <option value="algebra">Álgebra</option>
            <option value="geometria">Geometria</option>
          </select>
        </div>
        <!-- Tabela de Perguntas -->
    <div class="perguntas-disponiveis">
      <h2>Perguntas</h2>
      <table>
        <thead>
          <tr>
            <th>Selecionar</th>
            <th>Pergunta</th>
            <th>Complexidade</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(pergunta, index) in perguntasFiltradas" :key="index">
            <td>
              <input 
                type="checkbox" 
                :disabled="perguntasSelecionadas.length >= 10 && !pergunta.selecionada"
                v-model="pergunta.selecionada" 
                @change="selecionarPergunta(pergunta)"
              />
            </td>
            <td>{{ pergunta.texto }}</td>
            <td :class="getComplexidadeClass(pergunta.complexidade)">
              {{ pergunta.complexidade }}
            </td>
          </tr>
        </tbody>
      </table>
      <p>Total de perguntas selecionadas: {{ perguntasSelecionadas.length }}/10</p>
    </div>

    <!-- Perguntas Selecionadas -->
    <div class="perguntas-selecionadas">
      <h2>Perguntas Selecionadas</h2>
      <ul>
        <li v-for="(pergunta, index) in perguntasSelecionadas" :key="index">
          {{ pergunta.texto }} (Complexidade: {{ pergunta.complexidade }})
        </li>
      </ul>
    </div>
        <button type="submit">Cadastrar Jogo</button>
      </form>
    </div>
  </template>
  
  <script>
export default {
  data() {
    return {
      filtro: {
        serie: '',
        conteudo: '',
      },
      nome:'',
      perguntas: [
        { texto: 'Qual é o valor de 2 + 2?', complexidade: 'fácil', serie: '6', conteudo: 'aritmetica', selecionada: false },
        { texto: 'Qual é o resultado de 5 * 6?', complexidade: 'fácil', serie: '7', conteudo: 'aritmetica', selecionada: false },
        { texto: 'Qual é a raiz quadrada de 144?', complexidade: 'médio', serie: '8', conteudo: 'algebra', selecionada: false },
        { texto: 'Resolva a equação: 2x + 3 = 7', complexidade: 'médio', serie: '9', conteudo: 'algebra', selecionada: false },
        { texto: 'Qual é o valor do determinante da matriz 3x3?', complexidade: 'difícil', serie: '9', conteudo: 'geometria', selecionada: false },
        // Adicione mais perguntas aqui...
      ],
      perguntasFiltradas: [],
    };
  },
  mounted() {
    this.filtrarPerguntas();
  },
  computed: {
    perguntasSelecionadas() {
      return this.perguntas.filter(pergunta => pergunta.selecionada);
    }
  },
  methods: {
    getComplexidadeClass(complexidade) {
      if (complexidade === 'fácil') return 'facil';
      if (complexidade === 'médio') return 'medio';
      if (complexidade === 'difícil') return 'dificil';
      return '';
    },
    filtrarPerguntas() {
      this.perguntasFiltradas = this.perguntas.filter(pergunta => {
        return (!this.filtro.serie || pergunta.serie === this.filtro.serie) &&
               (!this.filtro.conteudo || pergunta.conteudo === this.filtro.conteudo);
      });
    },
    selecionarPergunta(pergunta) {
      if (pergunta.selecionada && this.perguntasSelecionadas.length >= 10) {
        pergunta.selecionada = false;
      }
    },
    configurarJogo() {
      // Aqui você pode adicionar a lógica para configurar o jogo com as perguntas selecionadas
      console.log("Perguntas selecionadas para o jogo:", this.perguntasSelecionadas);
    }
  }
};
</script>
  
  <style scoped>
  .cadastro-jogo {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
  }
  
  h2 {
    text-align: center;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input,
  select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #000064;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 10px;
  text-align: left;
  border: 1px solid #ccc;
}

.facil {
  color: green;
}

.medio {
  color: orange;
}

.dificil {
  color: red;
}

  </style>
  