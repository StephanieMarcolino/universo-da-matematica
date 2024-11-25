from rest_framework import serializers
from app.models import Professor, Turma, Jogo, Questao, Aluno, Categoria, Questao_Jogo, Jogo_Turma, Turma_Aluno

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
    perguntas = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )

    class Meta:
        model = Jogo
        fields = ['id', 'titulo', 'categoria', 'data', 'pin', 'perguntas']

    def create(self, validated_data):
        perguntas_ids = validated_data.pop('perguntas', [])
        jogo = Jogo.objects.create(**validated_data)

        # Cria associações no modelo intermediário
        for questao_id in perguntas_ids:
            questao = Questao.objects.filter(id=questao_id).first()
            if questao:
                Questao_Jogo.objects.create(jogo=jogo, questao=questao)

        return jogo

class QuestaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questao
        fields ="__all__" 
        #fields = ('id', 'descricao', 'classificacao')  

class QuestaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questao
        fields = '__all__'
        
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'pontuacao', 'progresso'] 
        extra_kwargs = {
            'nome': {'required': False},  # Torne o campo 'nome' não obrigatório
        }

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

class TurmaAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma_Aluno
        fields = ['turma', 'aluno'] 
        
                 
