# Generated by Django 5.1.2 on 2024-12-18 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_professor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name='email'),
        ),
    ]