# Generated by Django 4.0.5 on 2022-11-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_remove_autor_data_nasc_remove_autor_sexo_autor_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='foto',
            field=models.ImageField(upload_to='capas/'),
        ),
    ]
