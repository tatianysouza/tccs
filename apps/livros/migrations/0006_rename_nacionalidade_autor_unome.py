# Generated by Django 4.0.5 on 2022-11-22 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0005_alter_livro_capa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='nacionalidade',
            new_name='unome',
        ),
    ]