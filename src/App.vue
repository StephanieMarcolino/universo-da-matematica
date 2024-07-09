<template>
  <TelaMapa v-if="isMapaPage"/>

  <TelaPergunta v-if="isPerguntaPage"/>
  
  <TelaLogin v-if="isLoginPage" />

<TelaCadastro v-if="isCadastroPage" />
</template>

<script>
import TelaMapa from './views/TelaMapa.vue'
import TelaLogin from '@/views/TelaLogin.vue'
import TelaCadastro from '@/views/TelaCadastro.vue'
import TelaPergunta from '@/views/TelaPergunta.vue'

export default {
  name: 'App',
  components: {
    TelaMapa,
    TelaLogin,
    TelaCadastro, 
    TelaPergunta
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
  }
};
</script>

<style>

</style>
