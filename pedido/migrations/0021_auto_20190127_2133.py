# Generated by Django 2.0.10 on 2019-01-27 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0020_auto_20190127_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]