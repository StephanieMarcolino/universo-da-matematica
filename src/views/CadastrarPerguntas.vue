<template>
  <div class="criar-pergunta">
    <h2>Criar Nova Pergunta</h2>
    <form @submit.prevent="criarPergunta">
      <div class="form-group">
        <label for="descricao">Descrição da Pergunta</label>
        <textarea id="descricao" v-model="pergunta.descricao" required></textarea>
      </div>
      <div class="form-group">
        <label>Alternativas</label>
        <div v-for="(alternativa, index) in pergunta.alternativas" :key="index" class="alternativa-group">
          <input type="text" v-model="alternativa.texto" :placeholder="`Alternativa ${index + 1}`" required />
          <div class="d-flex align-items-center">
            <input type="radio" name="flexRadioDefault" id="flexRadioDefault{{ index }}" v-model="pergunta.correta" :value="index">
            <label class="form-check-label ms-2" :for="'flexRadioDefault' + index">
              Correta
            </label>
          </div>
        </div>
      </div>
      <div class="form-group">
        <label for="complexidade">Complexidade</label>
        <select id="complexidade" v-model="pergunta.complexidade" required>
          <option value="" disabled selected>Selecione</option>
          <option value="fácil">Fácil</option>
          <option value="médio">Médio</option>
          <option value="difícil">Difícil</option>
        </select>
      </div>
      <button type="submit">Salvar Pergunta</button>
    </form>
  </div>
</template>

  
  <script>
  export default {
    data() {
      return {
        pergunta: {
          descricao: '',
          alternativas: Array(4).fill({ texto: '' }), // 4 alternativas
          correta: null,
          complexidade: '',
        },
      };
    },
    methods: {
      criarPergunta() {
        // Lógica para salvar a pergunta
        console.log('Pergunta criada:', this.pergunta);
        // Limpar o formulário após a criação
        this.pergunta = {
          descricao: '',
          alternativas: Array(4).fill({ texto: '' }),
          correta: null,
          complexidade: '',
        };
        alert('Pergunta criada com sucesso!');
      },
    },
  };
  </script>
  
  <style scoped>
  .criar-pergunta {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
  }
  
  h2 {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  textarea,
  input,
  select {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
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

  .alternativa-group {
  display: flex;
  align-items: center;
  margin-bottom: 10px; /* Adiciona um espaço entre as alternativas */
}

.form-check-label {
  margin-left: 8px; /* Ajuste da margem para separar o texto do botão de rádio */
}

  </style>
  