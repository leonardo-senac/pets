# Generated by Django 4.2.4 on 2023-10-11 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
