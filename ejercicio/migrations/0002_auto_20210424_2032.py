# Generated by Django 2.2.20 on 2021-04-24 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejercicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirect',
            name='key',
            field=models.CharField(max_length=30, unique=True, verbose_name='key'),
        ),
    ]
