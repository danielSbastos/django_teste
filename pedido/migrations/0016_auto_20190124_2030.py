# Generated by Django 2.0.10 on 2019-01-24 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0015_auto_20190124_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]
