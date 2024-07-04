<template>
  <TelaMapa v-if="isMapaPage"/>
  
  <TelaLogin v-if="isLoginPage" />

<TelaCadastro v-if="isCadastroPage" />
</template>

<script>
import TelaMapa from './views/TelaMapa.vue'
import TelaLogin from '@/views/TelaLogin.vue'
import TelaCadastro from '@/views/TelaCadastro.vue'

export default {
  name: 'App',
  components: {
    TelaMapa,
    TelaLogin,
    TelaCadastro, 
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
  }
};
</script>

<style>

</style>
