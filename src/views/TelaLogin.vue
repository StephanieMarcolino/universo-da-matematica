<template>
    <div class="vh-100 vw-100 login-container">
        <div class="hello-login-container">
            <div class="hello-container">
                <div class="sm-7">
                    <h2 class="text-center">Olá</h2>
                    <h5 class="text-center">Bem-vindo de volta ao universo da matemática!</h5>
                </div>
            </div>
            <div class="login-form">
                <h2 class="text-center mb-5 title-login">Login</h2>
                <form @submit.prevent="submitForm">
                    <div class="mb-5 input-group">
                        <span class="input-group-text"><i class="fas fa-envelope"></i></span>
                        <input v-model="email" type="email" class="form-control" id="email" placeholder="Email" required>
                    </div>
                    <div class="mb-5 input-group">
                        <span class="input-group-text"><i class="fas fa-lock"></i></span>
                        <input v-model="password" type="password" class="form-control" id="password" placeholder="Senha"
                            required>
                    </div>
                    <div class="text-center">
                        <button type="button" class="btn btn-primary btn-block mb-3" @click="login">
                            <i class="fas fa-sign-in-alt"></i> Entrar
                        </button>
                        <hr/>
                        <button type="button" class="btn btn-outline-secondary btn-block" @click="registrar">
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
            alert('Login feito com sucesso');
            this.$router.push('/mapa');
        },
        registrar() {
            this.$router.push('/cadastro');
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

.hello-login-container {
    display: flex;
    border-radius: 5px;
    flex-direction: column;
    align-items: center;
    max-width: 400px;
}

.hello-container {
    width: 100%;
    background: linear-gradient(90deg, #0097fc 0%, #051a77 100%);
    color: white;
    padding: 20px;
    margin-bottom: 0px;
}

.login-form {
    width: 100%;
    background-color: rgba(255, 255, 255, 0.8);
    padding: 20px;
}

.btn-primary {
    background: linear-gradient(90deg, #0097fc 0%, #051a77 100%);
    box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
}

.btn-primary:hover,
.btn-outline-secondary:hover {
    background-color: #0097fc;
    border-color: #0097fc;
    color: white;
}

</style>
  