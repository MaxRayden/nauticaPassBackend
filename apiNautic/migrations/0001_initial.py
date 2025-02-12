# Generated by Django 5.1.4 on 2024-12-11 01:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('localizacao', models.CharField(max_length=255)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='pontos_turisticos/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TipoBarco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Barco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=255)),
                ('capacidade', models.PositiveIntegerField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='barcos/')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barcos', to='apiNautic.tipobarco')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('data_partida', models.DateTimeField()),
                ('data_chegada', models.DateTimeField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('barco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viagens', to='apiNautic.barco')),
                ('ponto_turistico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viagens', to='apiNautic.pontoturistico')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
