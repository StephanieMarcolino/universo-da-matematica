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
            <label class="form-check-label ms-2" :for="'flexRadioDefault' + index">Correta</label>
          </div>
        </div>
      </div>
      <div class="form-group">
        <label for="complexidade">Complexidade</label>
        <select id="complexidade" v-model="pergunta.classificacao" required>
          <option value="" disabled selected>Selecione</option>
          <option value="fácil">Fácil</option>
          <option value="médio">Médio</option>
          <option value="difícil">Difícil</option>
        </select>
      </div>
      <div class="form-group">
        <label for="categoria" class="me-2">Conteúdo</label>
        <div class="form-group d-flex align-items-center">
        <select v-model="categoria"  id="categoria" required>
          <option value="" disabled selected>Selecione</option>
          <option v-for="(categoria) in categorias" :key="categoria.id" :value="categoria.id">{{ categoria.descricao }}</option>
        </select>
        <button type="button" class="btn btn-secondary" @click="abrirModalCategoria">+</button>
      </div>
      </div>
      <button class="btn-salvar" type="submit">Salvar Pergunta</button>
    </form>

    <!-- Modal para cadastro de categoria -->
    <div v-if="mostrarModalCategoria" class="modal">
      <div class="modal-content">
        <span class="close" @click="fecharModalCategoria">&times;</span>
        <h3>Novo Conteúdo</h3>
        <form @submit.prevent="cadastrarCategoria">
          <div class="form-group">
            <label for="novaCategoria">Descrição</label>
            <input type="text" id="novaCategoria" v-model="novaCategoria.descricao" required />
          </div>
          <button class="btn-salvar" type="submit">Salvar Conteúdo</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pergunta: {
        descricao: '',
        alternativas: Array(4).fill(null).map(() => ({ texto: '' })),
        correta: null,
        classificacao: '',
      },
      categorias: [],
      categoria: '',
      mostrarModalCategoria: false,
      novaCategoria: {
        descricao: ''
      },
    };
  },
  mounted() {
    this.buscarCategorias();
  },
  methods: {
    async buscarCategorias() {
      try {
        const response = await fetch(`http://127.0.0.1:8000/categoria/vizualizar/`);
        const data = await response.json();
        this.categorias = data;
      } catch (error) {
        console.error('Erro ao buscar as categorias da API:', error);
      }
    },
    abrirModalCategoria() {
      this.mostrarModalCategoria = true;
    },
    fecharModalCategoria() {
      this.mostrarModalCategoria = false;
      this.novaCategoria.descricao = '';
    },
    async cadastrarCategoria() {
      try {
        const response = await fetch('http://127.0.0.1:8000/categoria/cadastrar/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.novaCategoria),
        });
        if (!response.ok) {
          throw new Error('Erro ao cadastrar categoria.');
        }
        this.fecharModalCategoria();
        this.buscarCategorias();
        alert('Categoria cadastrada com sucesso!');
      } catch (error) {
        console.error('Erro ao cadastrar categoria:', error);
        alert('Erro ao cadastrar categoria.');
      }
    },
    async criarPergunta() {
      try {
        // Construindo o payload para enviar ao backend
        const payload = {
          descricao: this.pergunta.descricao,
          classificacao: this.pergunta.classificacao,
          alternativa1: this.pergunta.alternativas[0]?.texto || '',
          alternativa2: this.pergunta.alternativas[1]?.texto || '',
          alternativa3: this.pergunta.alternativas[2]?.texto || '',
          resposta: this.pergunta.alternativas[this.pergunta.correta]?.texto || '',
          categoria: this.categoria,
        };
        // Validar antes de enviar (opcional)
        if (!payload.descricao || !payload.classificacao || !payload.resposta) {
          throw new Error('Todos os campos obrigatórios devem ser preenchidos.');
        }
        // Enviar a requisição para o backend
        const response = await fetch('http://127.0.0.1:8000/questoes/cadastrar/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(payload),
        });

        // Verificar a resposta do servidor
        if (!response.ok) {
          const errorData = await response.json();
          console.error('Erro da API:', errorData);
          throw new Error(errorData.detail || 'Erro ao criar pergunta');
        }

        const data = await response.json();
        console.log('Pergunta criada com sucesso:', data);

        // Limpar o formulário
        this.pergunta = {
          descricao: '',
          alternativas: Array(4).fill(null).map(() => ({ texto: '' })),
          correta: null,
          classificacao: '',
        };

        alert('Pergunta criada com sucesso!');
      } catch (error) {
        console.error('Erro ao criar pergunta:', error.message);
        alert(error.message);
      }
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

.btn-salvar {
  width: 100%;
  padding: 10px;
  background-color: #000064;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-salvar:hover {
  background-color: #0056b3;
}

.alternativa-group {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  /* Adiciona um espaço entre as alternativas */
}

.form-check-label {
  margin-left: 8px;
  /* Ajuste da margem para separar o texto do botão de rádio */
}
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  width: 300px;
  position: relative;
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  font-size: 18px;
  font-weight: bold;
}

button {
  cursor: pointer;
}
</style>
