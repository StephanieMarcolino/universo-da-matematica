<template>
    <div class="vh-100 vw-100 cadastro-container">
        <div class="content-center">
            <h2 class="text-center mb-5 cadastro-text">Faça o Cadastro</h2>
            <div sm="7" class="cadastro-form">
                
                <form @submit.prevent="submitForm">
                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-user"></i></span>
                            <input v-model="nome" type="text" class="form-control" id="nome" placeholder="Nome Completo*" required>
                        </div>
                    </div>
                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-id-badge"></i></span>
                            <input v-model="usuario" type="text" class="form-control" id="usuario" placeholder="Nome de Usuário*"
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
            usuario: '',
            senha: ''
        };
    },
    methods: {
        async cadastrar() {
            alert('Cadastro realizado com sucesso!');
            this.$router.push('/login-aluno');
        },
        voltar() {
            this.$router.push('/login-aluno');
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

.cadastro-form {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 20px;
    border-radius: 5px;
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

.content-center {
    text-align: center;
    max-width: 400px;
    width: 100%;
}

.cadastro-text {
    color: white;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 20px;
}
</style>