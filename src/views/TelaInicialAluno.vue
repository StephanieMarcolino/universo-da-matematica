<template>
    <div class="vh-100 vw-100 login-container">
        <LoadSpinner :isLoading="loadingSubmit" />
        <div class="top-right">
            <button class="btn btn-outline-secondary btn-block">
                <a
                    href="https://docs.google.com/forms/d/e/1FAIpQLScyq2Y2hHM47ItDnxj5N4CQGOhGIAkSyV_vnXq70hx3ktWVAw/viewform?usp=sf_link">Questionário</a>
            </button>
            <button class="btn btn-outline-secondary btn-block" @click="professorLogin">
                Professor Login
            </button>
        </div>
        <div class="content-center">
            <h1 class="welcome-text">Bem-vindo ao Universo da Matemática</h1>
            <div class="login-form">
                <form @submit.prevent="submitForm">
                    <div class="mb-4 input-group">
                        <span class="input-group-text"><i class="fas fa-user"></i></span>
                        <input v-model="nome" type="text" class="form-control" id="nome" placeholder="Nome Completo" required>
                    </div>
                    <div class="mb-4 input-group">
                        <span class="input-group-text"><i class="fas fa-users"></i></span>
                        <select v-model="turma" class="form-control" id="turma" placeholder="Turma" required>
                            <option value="" disabled selected>Selecione uma turma</option>
                            <option v-for="(turma) in turmas" :key="turma.id" :value="turma.id">{{ turma.nome }}</option>
                        </select>
                    </div>
                    <div class="mb-4 input-group">
                        <span class="input-group-text"><i class="fas fa-lock"></i></span>
                        <input v-model="pin" type="text" class="form-control" id="pin" placeholder="Pin do Jogo" required>
                    </div>
                    <div class="text-center">
                        <button type="submit" class="btn btn-primary btn-block mb-4">
                            <i class="fas fa-sign-in-alt"></i> Entrar
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import LoadSpinner from '../components/LoadSpiner.vue';

export default {
    components: {
    LoadSpinner
  },
    data() {
        return {
            nome: '',
            pin: '',
            turma: '',
            turmas: [],
            jogo: '',
            loadingSubmit: false,
        };
    },
    mounted() {
        localStorage.clear();
        this.buscarTurmas();
    },
    methods: {
        async buscarTurmas() {
            try {
                const response = await fetch(`http://127.0.0.1:8000/turmas/vizualizar/`);
                const data = await response.json();
                this.turmas = data;
            } catch (error) {
                console.error('Erro ao buscar as turmas da API:', error);
            }
        },
        async submitForm() {
            
            if (!this.nome || !this.pin || !this.turma) {
                alert("Por favor, preencha todos os campos obrigatórios.");
                return;
            }
            await this.login();
        },
        async login() {
            this.loadingSubmit = true;
            try {
                const response = await fetch(`http://127.0.0.1:8000/jogo/${this.pin}/`);
                const data = await response.json();
                if (data.error) {
                    this.loadingSubmit = false;
                    alert("Pin não encontrado");
                } else {
                    this.loadingSubmit = false;

                    localStorage.setItem("jogoId", data.id);
                    await this.salvarAluno()
                    this.$router.push('/mapa');
                    
                }
            } catch (error) {
                this.loadingSubmit = false;

                console.error('Erro ao buscar dados da API:', error);
            }
        },
        async salvarAluno() {
            try {
                const response = await fetch('http://127.0.0.1:8000/alunos/cadastrar/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ nome: this.nome })
                });
                if (!response.ok) {
                    throw new Error(`Erro: ${response.status}`);
                }
                const data = await response.json();
                console.log('Aluno salvo com sucesso:', data);
                this.salvarTurmaAluno(data.id);
                localStorage.setItem("aluno", data.id);
            } catch (error) {
                console.error('Erro ao salvar dados na API:', error);
            }
        },
        async salvarTurmaAluno(alunoId) {
            try {
                const response = await fetch('http://127.0.0.1:8000/turma-aluno/cadastrar/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ aluno: alunoId, turma: this.turma })
                });
                if (!response.ok) {
                    throw new Error(`Erro: ${response.status}`);
                }
                const data = await response.json();
                console.log('Turma-Aluno salvo com sucesso:', data);
            } catch (error) {
                console.error('Erro ao salvar dados na API:', error);
            }
        },
        professorLogin() {
            this.$router.push('/login-professor');
        },
    }
};
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

.login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-image: url('../assets/fundo.jpg');
    background-size: cover;
    background-position: center;
    padding: 20px;
    position: relative;
}

.top-right {
    position: absolute;
    top: 20px;
    right: 20px;
}

.content-center {
    text-align: center;
    max-width: 400px;
    width: 100%;
}

.welcome-text {
    color: white;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 20px;
}

.login-form {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 20px;
    border-radius: 5px;
}

.mb-4 {
    margin-bottom: 1rem !important;
}

.btn-primary {
    background: linear-gradient(90deg, rgba(10, 10, 50, 1) 0%, rgba(0, 0, 100, 1) 100%);
    box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
    width: 100%;
}

.btn-outline-secondary {
    border-color: #ffffff;
    color: white;
    margin-left: 5px;
}

.btn-outline-secondary:hover {
    background-color: #0097fc;
    border-color: #0097fc;
    color: white;
}
</style>
