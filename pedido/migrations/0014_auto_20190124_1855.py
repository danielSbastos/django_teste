# Generated by Django 2.0.10 on 2019-01-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0013_auto_20190124_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_unit',
            field=models.FloatField(max_length=200),
        ),
    ]