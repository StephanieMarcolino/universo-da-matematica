<template>
    <div class="vh-100 vw-100 login-container">
        <div class="top-right">
            <button class="btn btn-outline-secondary btn-block" @click="professorLogin">
                Professor Login
            </button>
            <button class="btn btn-outline-secondary btn-block" @click="professorCadastro">
                Professor Cadastro
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
                        <span class="input-group-text"><i class="fas fa-lock"></i></span>
                        <input v-model="pin" type="text" class="form-control" id="pin" placeholder="Pin do Jogo" required>
                    </div>
                    <div class="text-center">
                        <button type="button" class="btn btn-primary btn-block mb-4" @click="login">
                            <i class="fas fa-sign-in-alt"></i> Entrar
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            nome: '',
            pin: '',
        };
    },
    methods: {
        async login() {
            alert('Login feito com sucesso');
            this.$router.push('/mapa');
        },
        professorLogin() {
            this.$router.push('/login-professor');
        },
        professorCadastro() {
            this.$router.push('/cadastro-professor');
        }
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
