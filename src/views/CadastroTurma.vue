<template>
    <div class="cadastro-turma">
        <h2>Cadastro de Turma</h2>
        <form @submit.prevent="cadastrarTurma">
            <div class="form-group">
                <label for="nomeTurma">Nome da Turma</label>
                <input type="text" id="nomeTurma" v-model="turma.nome" required placeholder="Digite o nome da turma" />
            </div>
            <div class="form-group">
                <label for="escola">Escola</label>
                <input type="text" id="escola" v-model="turma.escola" required placeholder="Digite o nome da escola" />
            </div>
            <div class="form-group">
                <label for="serie">Série</label>
                <select id="serie" v-model="turma.serie" required>
                    <option value="" disabled selected>Selecione a série</option>
                    <option value="6">6° série</option>
                    <option value="7">7° série</option>
                    <option value="8">8° série</option>
                    <option value="9">9° série</option>
                </select>
            </div>
            <div class="form-group">
                <label for="ano">Ano</label>
                <select id="ano" v-model="turma.ano" required>
                    <option value="" disabled selected>Selecione o ano</option>
                    <option v-for="year in availableYears" :key="year" :value="year">{{ year }}</option>
                </select>
            </div>
            <button type="submit">Cadastrar Turma</button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'CadastroTurmaComponent',
    data() {
        return {
            turma: {
                nome: '',
                escola: '',
                serie: '',
                ano: '',
            },
            availableYears: this.getAvailableYears(), // Obter anos disponíveis
        };
    },
    methods: {
        getAvailableYears() {
            const startYear = 2024; // Ano a partir do qual as turmas podem ser cadastradas
            const years = [];
            for (let year = startYear; year <= startYear + 10; year++) {
                years.push(year);
            }
            return years;
        },
        async cadastrarTurma() {
            try {
                const response = await fetch('http://127.0.0.1:8000/turmas/cadastrar/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.turma), // Envia os dados da turma em formato JSON
                });

                if (!response.ok) {
                    throw new Error('Erro ao cadastrar a turma');
                }

                // Limpar o formulário após o cadastro
                this.turma = {
                    nome: '',
                    escola: '',
                    serie: '',
                    ano: null,
                };
                alert('Turma cadastrada com sucesso!');
            } catch (error) {
                console.error('Erro:', error);
                alert('Falha ao cadastrar a turma.');
            }
        },
    },
};
</script>

<style scoped>
.cadastro-turma {
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
</style>
