import { createRouter, createWebHistory } from 'vue-router';
import TelaLogin from '@/views/TelaLogin.vue'
import TelaCadastro from '@/views/TelaCadastro.vue'
import TelaMapa from '@/views/TelaMapa.vue';

const routes = [
  
  {
    path: '/cadastro',
    name: 'cadastro',
    component: TelaCadastro, 
  },
  {
    path: '/login',
    name: 'login',
    component: TelaLogin, 
  },
  {
    path: '/',
    redirect: '/login' 
  }, 
  {
    path: '/mapa',
    name: 'mapa',
    component: TelaMapa, 
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;