# Generated by Django 4.0.5 on 2022-11-22 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0006_rename_nacionalidade_autor_unome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orientador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnome', models.CharField(max_length=50, verbose_name='Primeiro nome:')),
                ('unome', models.CharField(max_length=50, verbose_name='Ultimo nome:')),
                ('link_curriculo', models.URLField()),
            ],
        ),
    ]
