# Generated by Django 5.1.2 on 2024-10-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_turma_serie_serie_remove_turma_serie_turma_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='nome')),
                ('pontuacao', models.IntegerField(default=0)),
                ('progresso', models.IntegerField(default=0)),
            ],
        ),
    ]
