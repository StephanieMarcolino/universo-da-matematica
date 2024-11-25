import { createRouter, createWebHistory } from 'vue-router';
import TelaLoginProfessor from '@/views/LoginProfessor.vue'
import TelaCadastroProfessor from '@/views/CadastroProfessor.vue'
import TelaMapa from '@/views/Mapa.vue';
import TelaPergunta from '@/views/TelaPerguntas.vue'
import TelaInicialAluno from '@/views/TelaInicialAluno.vue';
import TelaInicial from '@/views/TelaInicial.vue'
import TelaImprimirJogos from '@/views/ImprimirJogos.vue';
import TelaDetalheJogo from '@/views/DetalheJogoBaixar.vue';
import TelaCadastroTurma from '@/views/CadastroTurma.vue';
import VisualizarTurmas from '@/views/VisualizarTurmas.vue';
import DetalhesTurma from '@/views/DetalhesTurma.vue';
import CadastrarJogo from '@/views/CadastrarJogo.vue';
import CadastrarPerguntas from '@/views/CadastrarPerguntas.vue';
import VisualizarJogos from '@/views/VisualizarJogos.vue';
import DetalhesJogo from '@/views/DetalhesJogo.vue';
import MeuPerfil from '@/views/MeuPerfil.vue';

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
  { path: '/turmas', 
    name: 'VisualizarTurmas', 
    component: VisualizarTurmas 
  },
  { path: '/turmas/:turmaId', 
    name: 'DetalhesTurma', 
    component: DetalhesTurma 
  },
  { path: '/cadastrar-perguntas', 
    name: 'CadastrarPerguntas', 
    component: CadastrarPerguntas 
  },
  { path: '/cadastrar-jogo', 
    name: 'CadastrarJogo', 
    component: CadastrarJogo 
  },
  { path: '/jogos', 
    name: 'VisualizarJogos', 
    component: VisualizarJogos 
  },
  { path: '/jogos/:jogoId', 
    name: 'DetalhesJogo', 
    component: DetalhesJogo 
  },
  { path: '/meu-perfil', 
    name: 'MeuPerfil', 
    component: MeuPerfil 
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;