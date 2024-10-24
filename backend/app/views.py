from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from app.models import Professor, Turma, Jogo, Questao, Aluno, Categoria, Questao_Jogo, Jogo_Turma, Turma_Aluno
from .serializers import ProfessorSerializer, TurmaSerializer, JogoSerializer, QuestaoSerializer, AlunoSerializer, CategoriaSerializer, QuestaoJogoSerializer, JogoTurmaSerializer, TurmaAlunoSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

class ProfessorMenuView(APIView):
    permission_classes = [AllowAny]  # Permite que qualquer um acesse essa view

    def post(self, request):
        email = request.data.get('email')
        nome = request.data.get('nome')
        senha = request.data.get('senha')

        user = authenticate(email=email, senha=senha)

        if user is not None:
            # Se o login for bem-sucedido, você pode retornar um token ou alguma informação do usuário
            return Response({'message': 'Login bem-sucedido', 'nome': user.nome}, status=status.HTTP_200_OK)
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
    