import json, logging
from rest_framework import generics, mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from app.models import Professor, Turma, Jogo, Questao, Aluno, Categoria, Questao_Jogo, Jogo_Turma, Turma_Aluno
from .serializers import ProfessorSerializer, TurmaSerializer, JogoSerializer, QuestaoSerializer, AlunoSerializer, CategoriaSerializer, QuestaoJogoSerializer, JogoTurmaSerializer, TurmaAlunoSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)

def cadastrarProfessor(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nome = data.get('nome')
        email = data.get('email')
        senha = data.get('senha')
        senhaHash = make_password(senha)
        novoProfessor = Professor(nome=nome, email=email, senha=senhaHash)
        novoProfessor.save()
        return JsonResponse({'message': 'Professor cadastrado com sucesso!'}, status=201)

@csrf_exempt
def autenticarProfessor(request):
    print(f"Request body: {request.body}")
    if request.method == 'POST':
        data = json.loads(request.body) 
        print(f"Data parsed: {data}")
        email = data.get('email') 
        senhaInput = data.get('senha')
        try:
            professor = Professor.objects.get(email=email)
        except Professor.DoesNotExist:
            return JsonResponse({'error': 'Professor nao encontrado!'}, status=404)
        
        if check_password(senhaInput, professor.senha):
            return JsonResponse({'message': 'Login bem-sucedido!'}, status=200)
        return JsonResponse({'error': 'Credenciais invalidas!'}, status=400)

class ProfessorMenuView(APIView):
    permission_classes = [AllowAny]  # Permite que qualquer um acesse essa view

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            return Response({'message': 'Login bem-sucedido'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

#ViewSet para o Professor
class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all() #ViewSet irá gerenciar todos os registros do modelo
    serializer_class = ProfessorSerializer #Conversão  de instâncias do modelo Professor em JSON

#Recuperar, Atualizar e Excluir para Professor
class ProfessorRetrieveUpdateDestroyAPIView(generics.GenericAPIView,mixins.RetrieveModelMixin,
                                            mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    #Recuperar   
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    #Atualizar
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    #Excluir
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 

class ProfessorListCreateAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer 

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 
    

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

#Listar e Criar para Turma
class TurmaListCreateAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer 

    #Listar
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    #Criar
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 
    
class TurmaRetrieveUpdateDestroyAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin,
                                        mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all() 
    serializer_class = JogoSerializer

class JogoListCreateAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer 

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 


class JogoRetrieveUpdateDestroyAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class QuestaoViewSet(viewsets.ModelViewSet):
    queryset = Questao.objects.all() 
    serializer_class = QuestaoSerializer

class QuestaoListCreateAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 
    

class QuestaoRetrieveUpdateDestroyAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin,
                                           mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    
class QuestaoFacilView(APIView):
    def get(self, request, *args, **kwargs):
        # Filtrar questões com a classificação 'fácil'
        questoes_facil = Questao.objects.filter(classificacao='Fácil')

        # Serializar as questões
        serializer = QuestaoSerializer(questoes_facil, many=True)
        
        # Retornar as questões
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all() 
    serializer_class = AlunoSerializer 

class AlunoRetrieveUpdateDestroyAPIView(generics.GenericAPIView,mixins.RetrieveModelMixin,
                                            mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    #Recuperar   
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    #Atualizar
    def put(self, request, *args, **kwargs):
        print(request.data)  # Adicione este log para verificar os dados recebidos
        return self.update(request, *args, **kwargs)

    #Excluir
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 
    
    
    
class AlunoListCreateAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer 

    #Listar
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    #Criar
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 


class CategoriaListCreateAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer 

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all() 
    serializer_class = CategoriaSerializer

class QuestaoJogoViewSet(viewsets.ModelViewSet):
    queryset = Questao_Jogo.objects.all()
    serializer_class = QuestaoJogoSerializer

class JogoTurmaViewSet(viewsets.ModelViewSet):
    queryset = Jogo_Turma.objects.all()
    serializer_class = JogoTurmaSerializer

class TurmaAlunoViewSet(viewsets.ModelViewSet):
    queryset = Turma_Aluno.objects.all()
    serializer_class = TurmaAlunoSerializer

class TurmaAlunoListCreateAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Turma_Aluno.objects.all()
    serializer_class = TurmaAlunoSerializer 

    #Listar
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    #Criar
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

# Rota para buscar jogo pelo pin
@api_view(['GET'])
def get_jogo_by_pin(request, pin):
    try:
        jogo = Jogo.objects.get(pin=pin)
        serializer = JogoSerializer(jogo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Jogo.DoesNotExist:
        return Response({"error": "Jogo não encontrado"}, status=status.HTTP_404_NOT_FOUND)

# Rota para listar questões de um jogo
@api_view(['GET'])
def get_questoes_by_jogo(request, jogo_id):
    try:
        questoes_jogo = Questao_Jogo.objects.filter(jogo__id=jogo_id)
        questoes = [qj.questao for qj in questoes_jogo]
        serializer = QuestaoSerializer(questoes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Jogo.DoesNotExist:
        return Response({"error": "Jogo não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_alunos_by_turma(request, turma_id):
    try:
        turma_alunos = Turma_Aluno.objects.filter(turma_id=turma_id)
        alunos = [ta.aluno for ta in turma_alunos]
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Turma.DoesNotExist:
        return Response({"error": "Turma não encontrada"}, status=status.HTTP_404_NOT_FOUND)