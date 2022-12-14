# Generated by Django 4.0.5 on 2022-11-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='data_nasc',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='sexo',
        ),
        migrations.AddField(
            model_name='autor',
            name='foto',
            field=models.ImageField(default=None, upload_to='capas/'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nacionalidade',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
