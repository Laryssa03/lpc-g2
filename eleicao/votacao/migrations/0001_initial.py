# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 23:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('cpf', models.CharField(max_length=11)),
                ('propostas', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Eleicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HoraDataI', models.DateTimeField(blank=True, null=True)),
                ('HoraDataF', models.DateTimeField(blank=True, null=True)),
                ('local', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Eleitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('cpf', models.CharField(max_length=11)),
                ('eleicao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='votacao.Eleicao')),
            ],
        ),
        migrations.CreateModel(
            name='SecConselho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('cpf', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=128)),
                ('votou', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Urna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votos', models.IntegerField(max_length=10)),
                ('branco', models.CharField(max_length=128)),
                ('candidato', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='votacao.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='token',
            name='urna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='votacao.Urna'),
        ),
        migrations.AddField(
            model_name='eleicao',
            name='sec',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='votacao.SecConselho'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='vaga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='votacao.Vaga'),
        ),
    ]
