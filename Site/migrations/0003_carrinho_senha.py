# Generated by Django 3.0 on 2020-01-02 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0002_carrinho'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='senha',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]