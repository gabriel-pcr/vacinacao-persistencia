# Generated by Django 5.0.1 on 2024-01-29 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacinacao', '0002_alter_agenda_data_situacao_alter_agenda_situacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='dose_vacina',
            field=models.IntegerField(default=1),
        ),
    ]
