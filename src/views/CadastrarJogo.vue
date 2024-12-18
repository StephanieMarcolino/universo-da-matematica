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
        <label for="categoria" class="me-2">Conteúdo</label>
        <select v-model="categoria" @change="filtrarPerguntas" id="categoria" required>
          <option value="" disabled selected>Selecione</option>
          <option v-for="(categoria) in categorias" :key="categoria.id" :value="categoria.id">{{ categoria.descricao }}</option>
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
            <td>{{ pergunta.descricao }}</td>
            <td :class="getComplexidadeClass(pergunta.classificacao)">
              {{ pergunta.classificacao }}
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
    nome: '',
    categoria: '',
    categorias: [],
    perguntas: [], 
    perguntasFiltradas: [], 
    pin: '', 
  };
},
mounted() {
  this.buscarCategorias();
  this.buscarPerguntas();
},
methods: {
  gerarPin() {
      return Math.floor(1000 + Math.random() * 9000);  // Gera um número entre 1000 e 9999
    },

  async buscarCategorias() {
    try {
      const response = await fetch(`http://127.0.0.1:8000/categoria/vizualizar/`);
      const data = await response.json();
      this.categorias = data;
    } catch (error) {
      console.error('Erro ao buscar categorias:', error);
    }
  },
  async buscarPerguntas() {
    try {
      const response = await fetch(`http://127.0.0.1:8000/questoes/vizualizar/`);
      const data = await response.json();
      this.perguntas = data.map(questao => ({
        ...questao,
        selecionada: false, // Adiciona uma propriedade para seleção no frontend
      }));
      console.log(this.perguntas)
      this.filtrarPerguntas();
    } catch (error) {
      console.error('Erro ao buscar perguntas:', error);
    }
  },
   async cadastrarJogo() {
      try {
        if (this.perguntasSelecionadas.length === 0) {
          alert('Selecione ao menos uma pergunta para cadastrar o jogo.');
          return;
        }

        const payload = {
          titulo: this.nome,
          categoria: this.categoria,
          perguntas: this.perguntasSelecionadas.map(pergunta => pergunta.id),
          pin: this.gerarPin(),  // Adiciona o PIN gerado ao payload
        };

        const response = await fetch('http://127.0.0.1:8000/jogos/cadastrar/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(payload),
        });

        if (!response.ok) {
          const errorData = await response.json();
          console.error('Erro ao cadastrar jogo:', errorData);
          throw new Error(errorData.detail || 'Erro ao cadastrar jogo');
        }

        const data = await response.json();
        this.pin = data.pin;  // Salva o PIN retornado da API

        alert('Jogo cadastrado com sucesso! PIN do jogo: ' + this.pin);

        // Limpar o formulário
        this.nome = '';
        this.categoria = '';
        this.perguntas.forEach(pergunta => (pergunta.selecionada = false));
        this.buscarPerguntas;
      } catch (error) {
        console.error('Erro ao cadastrar jogo:', error.message);
        alert(error.message);
      }
    },
  getComplexidadeClass(complexidade) {
  const complexidadeLower = complexidade.toLowerCase();
  if (complexidadeLower === 'fácil') return 'facil';
  if (complexidadeLower === 'médio') return 'medio';
  if (complexidadeLower === 'difícil') return 'dificil';
  return '';
},
    selecionarPergunta(pergunta) {
      if (pergunta.selecionada && this.perguntasSelecionadas.length >= 10) {
        pergunta.selecionada = false;
      }
    },
  filtrarPerguntas() {
  this.perguntasFiltradas = this.perguntas.filter(pergunta => {
    return !this.categoria || pergunta.categoria === this.categoria;
  });
}
},
computed: {
  perguntasSelecionadas() {
    return this.perguntas.filter(pergunta => pergunta.selecionada);
  },
},

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
  