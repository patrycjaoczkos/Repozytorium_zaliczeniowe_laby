# Generated by Django 5.1.3 on 2025-01-14 18:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0005_alter_osoba_plec'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko']},
        ),
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
