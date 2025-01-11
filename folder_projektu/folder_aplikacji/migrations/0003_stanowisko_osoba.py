# Generated by Django 5.1.3 on 2025-01-11 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0002_person_pseudonim'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stanowisko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=80)),
                ('opis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=40)),
                ('nazwisko', models.CharField(max_length=60)),
                ('plec', models.CharField(choices=[('K', 'Kobieta'), ('M', 'Mężczyzna'), ('I', 'Inna')], default='I', max_length=1)),
                ('stanowisko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folder_aplikacji.stanowisko')),
            ],
        ),
    ]
