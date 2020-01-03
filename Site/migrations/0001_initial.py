# Generated by Django 3.0.1 on 2020-01-01 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(max_length=80)),
                ('sobrenome', models.CharField(max_length=80)),
                ('nickname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('texto', models.CharField(max_length=700)),
            ],
        ),
    ]
