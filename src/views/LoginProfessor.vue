<template>
    <div class="vh-100 vw-100 login-container">
        
        <div class="content-center">
            <h2 class="text-center mb-4 login-text">Faça o Login</h2>
            <div class="login-form">
            <form @submit.prevent="submitForm">
                <div class="mb-3 input-group">
                    <span class="input-group-text"><i class="fas fa-envelope"></i></span>
                    <input v-model="email" type="email" class="form-control" id="email" placeholder="Email" required>
                </div>
                <div class="mb-3 input-group">
                    <span class="input-group-text"><i class="fas fa-lock"></i></span>
                    <input v-model="password" type="password" class="form-control" id="password" placeholder="Senha" required>
                </div>
                <div class="text-center">
                    <button type="button" class="btn btn-primary btn-block mb-2" @click="login">
                        <i class="fas fa-sign-in-alt"></i> Entrar
                    </button>
                    <hr />
                    <button type="button" class="btn btn-outline-secondary btn-block mb-2" @click="registrar">
                        <i class="fas fa-user-plus"></i> Não tenho conta
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
            email: '',
            password: '',
        };
    },
    methods: {
        async login() {
            this.$router.push('/inicio');
        },
        registrar() {
            this.$router.push('/cadastro-professor');
        }
    }
};
</script>
  
<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

.login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-image: url('../assets/fundo.jpg');
    background-size: cover;
    background-position: center;
    background-color: rgba(255, 255, 255, 0.8);
    padding: 20px;
}

.login-form {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 20px;
    border-radius: 5px;
    max-width: 400px;
    width: 100%;
}

.content-center {
    text-align: center;
    max-width: 400px;
    width: 100%;
}

.btn-primary {
    background: linear-gradient(90deg, rgba(10, 10, 50, 1) 0%, rgba(0, 0, 100, 1) 100%);
}

.btn-outline-secondary:hover {
    background-color: #0097fc;
    border-color: #0097fc;
    color: white;
}

.login-text {
    color: white;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 20px;
}
</style>
