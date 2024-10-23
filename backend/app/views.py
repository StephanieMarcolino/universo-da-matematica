from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from app.models import Professor, Turma, Jogo, Questao, Aluno, Categoria, Questao_Jogo, Jogo_Turma
from .serializers import ProfessorSerializer, TurmaSerializer, JogoSerializer, QuestaoSerializer, AlunoSerializer, CategoriaSerializer, QuestaoJogoSerializer, JogoTurmaSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class ProfessorMenuView(APIView):
    permission_classes = [AllowAny]  # Permite que qualquer um acesse essa view

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            # Se o login for bem-sucedido, você pode retornar um token ou alguma informação do usuário
            return Response({'message': 'Login bem-sucedido', 'username': user.username}, status=status.HTTP_200_OK)
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
    
class QuestaoListCreateAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 
    
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

class QuestaoJogoCreateView(generics.CreateAPIView):
    queryset = Questao_Jogo.objects.all()
    serializer_class = QuestaoJogoSerializer

class JogoTurmaCreateView(generics.CreateAPIView):
    queryset = Jogo_Turma.objects.all()
    serializer_class = JogoTurmaSerializer

