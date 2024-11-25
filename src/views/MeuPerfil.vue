<template>
    <div class="meu-perfil">
        <h2>Meu Perfil</h2>

        <div class="perfil-info">
            <div class="form-group">
                <label for="nome">Nome</label>
                <input type="text" id="nome" v-model="usuario.nome" required placeholder="Digite seu nome" />
            </div>

            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" v-model="usuario.email" required placeholder="Digite seu email" />
            </div>

            <div class="form-group">
                <label for="senha">Senha</label>
                <input type="password" id="senha" v-model="usuario.senha" required placeholder="Digite sua senha" />
            </div>

            <button @click="salvarPerfil">Salvar Alterações</button>
        </div>

        <div v-if="perfilSalvo" class="success-message">
            <p>Perfil salvo com sucesso!</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'MeuPerfil',
    data() {
        return {
            usuario: {
                nome: '', 
                email: '', 
                senha: '', 
            },
            perfilSalvo: false,
        };
    },
    methods: {
        salvarPerfil() {
            console.log('Perfil salvo:', this.usuario);

           
            // alterando a flag de sucesso para mostrar a mensagem.
            this.perfilSalvo = true;

            setTimeout(() => {
                this.perfilSalvo = false;
            }, 3000); // Mensagem visível por 3 segundos
        },
    },
};
</script>

<style scoped>
.meu-perfil {
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

input {
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

.success-message {
    margin-top: 20px;
    padding: 10px;
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
    border-radius: 5px;
    text-align: center;
}
</style>
