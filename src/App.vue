<template>
  <TelaMapa v-if="isMapaPage" />

  <TelaMapaJogo2 v-if="isJogo2Page" />

  <TelaPergunta v-if="isPerguntaPage" />

  <TelaLoginProfessor v-if="isLoginPage" />

  <TelaCadastroProfessor v-if="isCadastroPage" />

  <TelaLoginAluno v-if="isLoginAlunoPage" />

  <TelaCadastroAluno v-if="isCadastroAlunoPage" />

  <TelaInicialAluno v-if="isInicioAlunoPage" />

  <NavbarComponent v-if="isProfessorPage" />
</template>

<script>
import TelaMapa from './views/Mapa.vue'
import TelaMapaJogo2 from './views/MapaJogo2.vue'
import TelaLoginProfessor from '@/views/LoginProfessor.vue'
import TelaCadastroProfessor from '@/views/CadastroAluno.vue'
import TelaLoginAluno from '@/views/LoginAluno.vue'
import TelaCadastroAluno from '@/views/CadastroAluno.vue'
import TelaPergunta from '@/views/TelaPerguntas.vue'
import TelaInicialAluno from '@/views/TelaInicialAluno.vue'
import NavbarComponent from '@/components/NavBarComponent.vue'

export default {
  name: 'App',
  components: {
    TelaMapa,
    TelaMapaJogo2,
    TelaLoginProfessor,
    TelaCadastroProfessor,
    TelaPergunta,
    TelaInicialAluno,
    NavbarComponent,
    TelaCadastroAluno,
    TelaLoginAluno
  },
  computed: {
    isLoginPage() {
      return this.$route.name === "login-professor";
    },
    isCadastroPage() {
      return this.$route.name === "cadastro-professor";
    },
    isLoginAlunoPage() {
      return this.$route.name === "login-aluno";
    },
    isCadastroAlunoPage() {
      return this.$route.name === "cadastro-aluno";
    },
    isMapaPage() {
      return this.$route.name === "mapa";
    },
    isJogo2Page() {
      return this.$route.name === "mapa-jogo2";
    },
    isPerguntaPage() {
      return this.$route.name === "pergunta";
    },
    isInicioAlunoPage() {
      return this.$route.name === "inicio-aluno";
    },
    isProfessorPage(){
      return this.$route.name !== "login" && this.$route.name !== "cadastro" && this.$route.name !== "mapa" && this.$route.name !== "pergunta" && this.$route.name !== "inicio-aluno";
    }
  }
};
</script>

<style></style>
