# Generated by Django 2.0.10 on 2019-01-24 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0005_auto_20190123_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='multiplo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='preco_unit',
            field=models.FloatField(default=True),
        ),
    ]