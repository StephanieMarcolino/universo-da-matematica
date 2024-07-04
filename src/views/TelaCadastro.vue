<template>
    <div class="vh-100 vw-100 cadastro-container">
        <div class="hello-cadastro-container">
            <div class="hello-container">
                <div class="sm-7">
                    <h2 class="text-center">Olá</h2>
                    <h5 class="text-center">Bem-vindo ao universo da matemática!</h5>
                </div>
            </div>
            <div sm="7" class="cadastro-form">
                <h2 class="text-center mb-5 title-cadastro">Faça o cadastro</h2>
                <form @submit.prevent="submitForm">
                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-user"></i></span>
                            <input v-model="nome" type="text" class="form-control" id="nome" placeholder="Nome*" required>
                        </div>
                    </div>
                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-envelope"></i></span>
                            <input v-model="email" type="email" class="form-control" id="email" placeholder="Email*"
                                required>
                        </div>
                    </div>
                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-lock"></i></span>
                            <input v-model="senha" type="password" class="form-control" id="senha" placeholder="Senha*"
                                required>
                        </div>
                    </div>
                    <div class="text-center">
                        <button type="button" class="btn btn-primary btn-block" @click="cadastrar">
                            <i class="fas fa-sign-in-alt"></i> Cadastrar
                        </button>
                        <hr />
                        <button type="button" class="btn btn-outline-secondary" @click="voltar">
                            <i class="fas fa-arrow-left"></i> Voltar
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
            email: '',
            senha: ''
        };
    },
    methods: {
        async cadastrar() {
            alert('Cadastro realizado com sucesso!');
            this.$router.push('/login');
        },
        voltar() {
            this.$router.push('/login');
        }
    }
};
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

.cadastro-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-image: url('../assets/fundo.jpg');
    background-size: cover;
    background-position: center;
}

.hello-cadastro-container {
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

.cadastro-form {
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