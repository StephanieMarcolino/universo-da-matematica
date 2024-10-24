"""
URL configuration for backend project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from app.views import ProfessorMenuView  

from app.views import (
    ProfessorMenuView,
    ProfessorViewSet,
    ProfessorListCreateAPIView,
    ProfessorRetrieveUpdateDestroyAPIView,
    TurmaViewSet,
    TurmaListCreateAPIView,
    TurmaRetrieveUpdateDestroyAPIView,
    JogoViewSet,
    JogoListCreateAPIView,
    JogoRetrieveUpdateDestroyAPIView,
    QuestaoViewSet,
    QuestaoListCreateAPIView,
    QuestaoRetrieveUpdateDestroyAPIView, 
    QuestaoFacilView,
    AlunoViewSet,
    AlunoListCreateAPIView,
    AlunoRetrieveUpdateDestroyAPIView,
    CategoriaViewSet,
    CategoriaListCreateAPIView,
    QuestaoJogoViewSet,
    JogoTurmaViewSet,
    TurmaAlunoViewSet,
    TurmaAlunoListCreateAPIView,
    get_jogo_by_pin,
    get_questoes_by_jogo,
    
)

router = routers.DefaultRouter()
router.register(r'professores', ProfessorViewSet)

urlpatterns = [
    path('/',include(router.urls)),


    #tokens
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Rotas para Professor
    path('professor/vizualizar/', ProfessorViewSet.as_view({'get': 'list'})),
    path('professor/menu/', ProfessorMenuView.as_view(), name='menu-professor'),
    path('professor/cadastrar/', ProfessorListCreateAPIView.as_view(), name='professor-list-create'),
    path('professor/<int:pk>/', ProfessorRetrieveUpdateDestroyAPIView.as_view(), name='professor-detail'),

    # Rotas para Aluno
    path('alunos/vizualizar/', AlunoViewSet.as_view({'get': 'list'})),
    path('alunos/cadastrar/', AlunoListCreateAPIView.as_view(), name='aluno-list-create'),
    path('alunos/<int:pk>/', AlunoRetrieveUpdateDestroyAPIView.as_view(), name='aluno-detail'),

    # Rotas para Turma
    path('turmas/vizualizar/', TurmaViewSet.as_view({'get': 'list'})),
    path('turmas/cadastrar/', TurmaListCreateAPIView.as_view(), name='turma-list-create'),
    path('turmas/<int:pk>/', TurmaRetrieveUpdateDestroyAPIView.as_view(), name='turma-detail'),
    
    # Rotas para Jogo
    path('jogos/vizualizar/', JogoViewSet.as_view({'get': 'list'})),
    path('jogos/cadastrar/', JogoListCreateAPIView.as_view(), name='jogos-list-create'),
    path('jogos/<int:pk>/', JogoRetrieveUpdateDestroyAPIView.as_view(), name='jogo-detail'),
    
    # Rotas para Questao
    path('questoes/vizualizar/', QuestaoViewSet.as_view({'get': 'list'})),
    path('questoes/cadastrar/', QuestaoListCreateAPIView.as_view(), name='questao-list-create'),
    path('questoes/<int:pk>/', QuestaoRetrieveUpdateDestroyAPIView.as_view(), name='questao-detail'),
    path('questoes/facil/', QuestaoFacilView.as_view(), name='questoes_facil'), 

    # Rota para categoria
    path('categoria/vizualizar/', CategoriaViewSet.as_view({'get': 'list'})),
    path('categoria/cadastrar/', CategoriaListCreateAPIView.as_view(), name='categoria-list-create'),

    # Rotas para questao-jogo
    path('questao-jogo/vizualizar/', QuestaoJogoViewSet.as_view({'get': 'list'})),

    # Rotas para jogo-turma
    path('jogo-turma/vizualizar/', JogoTurmaViewSet.as_view({'get': 'list'})),

    # Rotas para turma-aluno
    path('turma-aluno/vizualizar/', TurmaAlunoViewSet.as_view({'get': 'list'})),
    path('turma-aluno/cadastrar/', TurmaAlunoListCreateAPIView.as_view(), name='turma-aluno-list-create'),

    # Rotas para pegar um jogo pelo pin
    path('jogo/<str:pin>/', get_jogo_by_pin, name='get_jogo_by_pin'),

    # Rotas para pegar questçoes de um jogo
    path('jogo/<int:jogo_id>/questoes/', get_questoes_by_jogo, name='get_questoes_by_jogo'),

]
