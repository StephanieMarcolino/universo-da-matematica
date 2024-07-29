import { createRouter, createWebHistory } from 'vue-router';
import TelaLogin from '@/views/TelaLogin.vue'
import TelaCadastro from '@/views/TelaCadastro.vue'
import TelaMapa from '@/views/TelaMapa.vue';
import TelaPergunta from '@/views/TelaPergunta.vue'
import TelaLoginAluno from '@/views/TelaLoginAluno.vue';
import TelaInicial from '@/views/TelaInicial.vue'
import TelaImprimirJogos from '@/views/TelaImprimirJogos.vue';
import TelaDetalheJogo from '@/views/TelaDetalheJogo.vue';
import TelaCadastroTurma from '@/views/TelaCadastroTurma.vue';

const routes = [
  
  {
    path: '/cadastro-professor',
    name: 'cadastro',
    component: TelaCadastro, 
  },
  {
    path: '/login-professor',
    name: 'login',
    component: TelaLogin, 
  },
  {
    path: '/login-aluno',
    name: 'login-aluno',
    component: TelaLoginAluno, 
  },
  {
    path: '/',
    redirect: '/login-aluno' 
  }, 
  {
    path: '/mapa',
    name: 'mapa',
    component: TelaMapa, 
  },
  {
    path: '/pergunta/:id',
    name: 'pergunta',
    component: TelaPergunta,
    props: true, 
  },
  {
    path: '/inicio',
    name: 'inicio',
    component: TelaInicial, 
  },
  {
    path: '/imprimir-jogos',
    name: 'imprimir-jogos',
    component: TelaImprimirJogos, 
  },
  {
    path: '/imprimir-jogos/jogo/:id',
    name: 'imprimir-jogo-detalhe',
    component: TelaDetalheJogo, 
    props:true
  },
  {
    path: '/cadastro-turma',
    name: 'cadastro-turma',
    component: TelaCadastroTurma, 
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;