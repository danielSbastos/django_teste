# Generated by Django 2.0.10 on 2019-01-24 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0009_cadastro_preco_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='qtd',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='preco_unit',
            field=models.FloatField(default=True),
        ),
    ]
