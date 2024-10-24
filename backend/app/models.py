from django.db import models


class Professor(models.Model):
    nome = models.CharField('nome', max_length=255, null=True, blank=False)
    email = models.CharField('email', max_length=255, null=True, blank=False)
    senha = models.CharField('senha', max_length=64, null=True, blank=False)
    data = models.DateTimeField(auto_now_add=True,  null=True)

class Turma(models.Model):
    nome = models.CharField('nome', max_length=100, null=False, blank=False)
    ano = models.DecimalField('ano', max_digits=4, decimal_places=0) #max_digits=4: xxxx
    escola = models.CharField('escola', max_length=255, null=False, blank=False)
    serie = models.CharField('serie', max_length=100, null=False, blank=False, default='9º ')
    
class Professor_Turma(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

class Categoria(models.Model):
    descricao = models.CharField('descricao', max_length=45, null=False, blank=False)

class Jogo(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField('titulo', max_length=255, null=False, blank=False)
    data = models.DateTimeField(auto_now_add=True,  null=False, blank=False)
    pin = models.IntegerField(default=0) 

class Jogo_Turma(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    
class Questao(models.Model):
    descricao = models.CharField('descricao',  max_length=255, null=False, blank=False)
    classificacao = models.CharField('classificacao', max_length=45, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    alternativa1 = models.CharField('alternativa1', max_length=100, null=False)
    alternativa2 = models.CharField('alternativa2', max_length=100, null=False)
    alternativa3 = models.CharField('alternativa3', max_length=100, null=False)
    resposta = models.CharField('resposta', max_length=100, null = False)
    
class Questao_Jogo(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)

class Aluno(models.Model):
    nome = models.CharField('nome', max_length=255, null=False, blank=False)
    pontuacao = models.IntegerField(default=0) 
    progresso = models.IntegerField(default=1) 

class Turma_Aluno(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    