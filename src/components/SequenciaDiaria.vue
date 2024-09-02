<template>
    <div v-if="visible" class="popup-overlay" @click="closePopup">
      <div class="popup-content" @click.stop>
        <h2 class="popup-title">Sequência Diária</h2>
        <div class="rocket-container">
          <img class="rocket-icon" src="@/assets/rocket.png" alt="Foguete" />
        </div>
        <p class="popup-message">
          Parabéns por manter sua sequência diária! Você está há 
          <span class="highlight">{{ accessedDays.length }}</span> dias jogando consecutivamente. 
          Se você não acessar o jogo por um dia, a sequência será reiniciada. Continue assim!
        </p>
        <button class="popup-close" @click="closePopup">Fechar</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      visible: {
        type: Boolean,
        default: false
      }
    },
    data() {
      return {
        accessedDays: [1, 2, 3], // IDs dos dias acessados
        totalDays: 7 // Número total de dias
      };
    },
    methods: {
      closePopup() {
        this.$emit('close');
      }
    }
  }
  </script>
  
  <style scoped>
  .popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .popup-content {
    background: #2e2e2e;
    color: #fff;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
    max-width: 400px; /* Define o tamanho máximo do popup */
    width: 90%; /* Ajusta a largura para caber bem em diferentes tamanhos de tela */
  }
  
  .popup-title {
    font-size: 1.5rem;
    margin-bottom: 10px;
  }
  
  .popup-message {
    margin-bottom: 20px;
    font-size: 1rem;
  }
  
  .highlight {
    font-size: 1.5rem; /* Aumenta o tamanho do número de dias */
    font-weight: bold;
    color: #6DC7FF; /* Cor de destaque */
  }
  
  .popup-close {
    background: linear-gradient(90deg, #1A6DFF, #C822FF);
  border: none;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  }
  
  .popup-close:hover {
    opacity: 0.5;
  }
  
  .rocket-container {
    margin: 20px 0;
  }
  
  .rocket-icon {
    width: 50px;
    height: 50px;
    animation: fly 2s linear infinite;
  }
  
  @keyframes fly {
    0% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0); }
  }
  </style>
  