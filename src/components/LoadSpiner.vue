<template>
  <div class="spinner" v-if="isLoading">
    <div class="loader"></div>
    <p>Carregando...</p>
  </div>
</template>

<script>
export default {
  name: 'LoadSpinner',
  props: {
    isLoading: {
      type: Boolean,
      required: true,
    },
  },
};
</script>

<style scoped>
.spinner {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh; /* Ajuste conforme necessário */
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.8); /* Fundo semi-transparente */
  z-index: 1000; /* Garantir que fique acima de outros conteúdos */
}

.loader {
  border: 8px solid #f3f3f3; /* Cor de fundo do spinner */
  border-top: 8px solid #3498db; /* Cor do spinner */
  border-radius: 50%;
  width: 50px; /* Ajuste conforme necessário */
  height: 50px; /* Ajuste conforme necessário */
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
