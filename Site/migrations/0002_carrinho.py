# Generated by Django 3.0.1 on 2020-01-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(max_length=80)),
                ('sobrenome', models.CharField(max_length=80)),
                ('nickname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=100)),
                ('valor', models.CharField(max_length=8)),
            ],
        ),
    ]