# Generated by Django 4.0.5 on 2022-11-17 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editora',
            name='estado',
        ),
    ]
