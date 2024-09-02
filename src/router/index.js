import { createRouter, createWebHistory } from 'vue-router';
import TelaLoginProfessor from '@/views/TelaLoginProfessor.vue'
import TelaCadastroProfessor from '@/views/TelaCadastroProfessor.vue'
import TelaLoginAluno from '@/views/TelaLoginAluno.vue'
import TelaCadastroAluno from '@/views/TelaCadastroAluno.vue'
import TelaMapa from '@/views/TelaMapa.vue';
import TelaMapaJogo2 from '@/views/TelaMapaJogo2.vue';
import TelaPergunta from '@/views/TelaPergunta.vue'
import TelaInicialAluno from '@/views/TelaInicialAluno.vue';
import TelaInicial from '@/views/TelaInicial.vue'
import TelaImprimirJogos from '@/views/TelaImprimirJogos.vue';
import TelaDetalheJogo from '@/views/TelaDetalheJogo.vue';
import TelaCadastroTurma from '@/views/TelaCadastroTurma.vue';

const routes = [
  
  {
    path: '/cadastro-professor',
    name: 'cadastro-professor',
    component: TelaCadastroProfessor, 
  },
  {
    path: '/login-professor',
    name: 'login-professor',
    component: TelaLoginProfessor, 
  },
  {
    path: '/cadastro-aluno',
    name: 'cadastro-aluno',
    component: TelaCadastroAluno, 
  },
  {
    path: '/login-aluno',
    name: 'login-aluno',
    component: TelaLoginAluno, 
  },
  {
    path: '/inicio-aluno',
    name: 'inicio-aluno',
    component: TelaInicialAluno, 
  },
  {
    path: '/',
    redirect: '/inicio-aluno' 
  }, 
  {
    path: '/mapa',
    name: 'mapa',
    component: TelaMapa, 
  },
  {
    path: '/jogo2/mapa',
    name: 'mapa-jogo2',
    component: TelaMapaJogo2, 
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