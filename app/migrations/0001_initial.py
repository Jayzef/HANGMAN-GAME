# Generated by Django 5.1.1 on 2024-09-23 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClasseDePalavra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NDC', models.CharField(max_length=100, verbose_name='Classe de palavra')),
            ],
            options={
                'verbose_name': 'Classe de palavra',
                'verbose_name_plural': 'Classe de palavras',
            },
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jogador', models.CharField(max_length=255, verbose_name='Jogador')),
                ('sequencia', models.CharField(max_length=255, verbose_name='Sequência')),
            ],
            options={
                'verbose_name': 'Jogo',
                'verbose_name_plural': 'Jogos',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nickname')),
                ('senha', models.CharField(max_length=100, verbose_name='Password')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='Palavra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palavra', models.CharField(max_length=20, verbose_name='Palavra')),
                ('dica', models.CharField(max_length=100, verbose_name='Dica da palavra')),
                ('CDP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classedepalavra', verbose_name='Classe da palavra')),
            ],
            options={
                'verbose_name': 'Palavra',
                'verbose_name_plural': 'palavras',
            },
        ),
    ]
