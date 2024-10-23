from rest_framework import serializers
from app.models import Professor, Turma, Jogo, Questao, Aluno, Categoria, Questao_Jogo, Jogo_Turma

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields ="__all__"
        #fields = ('id', 'nome', 'email')  

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields ="__all__"
        #fields = ('id', 'nome', 'ano')  

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields ="__all__"
        #fields = ('id', 'titulo', 'categoria')  

class QuestaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questao
        fields ="__all__" 
        #fields = ('id', 'descricao', 'classificacao')  

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields ="__all__"
           

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields ="__all__"       

class QuestaoJogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questao_Jogo
        fields = ['questao', 'jogo']    

class JogoTurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo_Turma
        fields = ['jogo', 'turma']  
