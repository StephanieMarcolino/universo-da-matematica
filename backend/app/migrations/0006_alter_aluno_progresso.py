# Generated by Django 4.2.5 on 2024-10-30 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_professor_email_alter_professor_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='progresso',
            field=models.IntegerField(default=1),
        ),
    ]
