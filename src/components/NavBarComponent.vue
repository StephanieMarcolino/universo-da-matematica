<template>
    <div>
      <nav class="navbar navbar-expand-lg navbar-dark bg-universe">
        <div class="container-fluid">
          <a class="navbar-brand" href="#"></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="/inicio">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/turmas">Visualizar Turmas</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/cadastro-turma">Criar Turma</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/cadastrar-jogo">Criar Jogo</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/cadastrar-perguntas">Criar Questões</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/imprimir-jogos">Imprimir Jogos</a>
              </li>
            </ul>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Perfil
                </a>
                <ul class="dropdown-menu dropdown-menu-end">
                    <li><a class="dropdown-item" href="/meuperfil"><i class="fas fa-user"></i> Meu Perfil</a></li>
                    <li><a class="dropdown-item" href="/login" @click="confirmAction"><i class="fas fa-sign-out-alt"></i> Sair</a></li>
                </ul>
              </li>
          </div>
        </div>
      </nav>
      <div class="content">
        <router-view></router-view>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'NavbarComponent',
  
    methods: {
      confirmAction() {
        if (confirm("Você tem certeza que deseja sair?")) {
          this.fazLogout();
        }
      },
      async fazLogout() {
        localStorage.clear();
        this.$router.push('/login-professor');
      }
    }
  }
  </script>
  
  <style scoped>
  @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    display: inline-block;
    margin: 0px;
  }
  
  a {
    color: #ffffff !important; 
    white-space: nowrap; 
    font-size: 1.1em; 
  }
  
  .nav-item .dropdown-item {
    display: flex;
    align-items: center;
    font-size: 1em;
    justify-content: center;
    color: #000; 
  }
  
  .nav-item .dropdown-item i {
    margin-right: 8px; 
  }
  
  .nav-item:hover {
    background-color: rgba(255, 255, 255, 0.1) !important; 
    color: #ffffff !important; 
  }
  
  .dropdown-menu {
    background-color: #1b1b2a; 
  }
  
  .dropdown-item:hover {
    background-color: rgba(255, 255, 255, 0.1); 
    color: #ffffff; 
  }
  
  /* Adiciona margem superior ao conteúdo para evitar sobreposição com o navbar */
  .content {
    margin-top: 50px;
  }
  
  .bg-universe {
    background: linear-gradient(90deg, rgba(10, 10, 50, 1) 0%, #000064 100%);
  }
  </style>
  