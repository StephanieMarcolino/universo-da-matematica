<template>
  <TelaMapa v-if="isMapaPage" />

  <TelaPergunta v-if="isPerguntaPage" />

  <TelaLogin v-if="isLoginPage" />

  <TelaCadastro v-if="isCadastroPage" />

  <TelaLoginAluno v-if="isLoginAlunoPage" />

  <NavbarComponent v-if="isProfessorPage" />
</template>

<script>
import TelaMapa from './views/TelaMapa.vue'
import TelaLogin from '@/views/TelaLogin.vue'
import TelaCadastro from '@/views/TelaCadastro.vue'
import TelaPergunta from '@/views/TelaPergunta.vue'
import TelaLoginAluno from '@/views/TelaLoginAluno.vue'
import NavbarComponent from '@/components/NavBarComponent.vue'

export default {
  name: 'App',
  components: {
    TelaMapa,
    TelaLogin,
    TelaCadastro,
    TelaPergunta,
    TelaLoginAluno,
    NavbarComponent
  },
  computed: {
    isLoginPage() {
      return this.$route.name === "login";
    },
    isCadastroPage() {
      return this.$route.name === "cadastro";
    },
    isMapaPage() {
      return this.$route.name === "mapa";
    },
    isPerguntaPage() {
      return this.$route.name === "pergunta";
    },
    isLoginAlunoPage() {
      return this.$route.name === "login-aluno";
    },
    isProfessorPage(){
      return this.$route.name !== "login" && this.$route.name !== "cadastro" && this.$route.name !== "mapa" && this.$route.name !== "pergunta" && this.$route.name !== "login-aluno";
    }
  }
};
</script>

<style></style>
