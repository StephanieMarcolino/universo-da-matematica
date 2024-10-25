<template>
  <TelaMapa v-if="isMapaPage" />

  <TelaPergunta v-if="isPerguntaPage" />

  <TelaLoginProfessor v-if="isLoginPage" />

  <TelaCadastroProfessor v-if="isCadastroPage" />

  <TelaInicialAluno v-if="isInicioAlunoPage" />

  <NavbarComponent v-if="isProfessorPage" />
</template>

<script>
import TelaMapa from './views/Mapa.vue'
import TelaLoginProfessor from '@/views/LoginProfessor.vue'
import TelaCadastroProfessor from '@/views/CadastroAluno.vue'
import TelaPergunta from '@/views/TelaPerguntas.vue'
import TelaInicialAluno from '@/views/TelaInicialAluno.vue'
import NavbarComponent from '@/components/NavBarComponent.vue'

export default {
  name: 'App',
  components: {
    TelaMapa,
    TelaLoginProfessor,
    TelaCadastroProfessor,
    TelaPergunta,
    TelaInicialAluno,
    NavbarComponent,
  },
  computed: {
    isLoginPage() {
      return this.$route.name === "login-professor";
    },
    isCadastroPage() {
      return this.$route.name === "cadastro-professor";
    },
    isMapaPage() {
      return this.$route.name === "mapa";
    },
    isPerguntaPage() {
      return this.$route.name === "pergunta";
    },
    isInicioAlunoPage() {
      return this.$route.name === "inicio-aluno";
    },
    isProfessorPage(){
      return this.$route.name !== "login-professor" && this.$route.name !== "cadastro-professor" && this.$route.name !== "mapa" && this.$route.name !== "pergunta" && this.$route.name !== "inicio-aluno";
    }
  }
};
</script>

<style></style>
