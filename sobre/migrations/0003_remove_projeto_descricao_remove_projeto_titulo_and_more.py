# Generated by Django 4.0.2 on 2022-03-02 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sobre', '0002_alter_projeto_options_projeto_descricao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='titulo',
        ),
        migrations.AddField(
            model_name='projeto',
            name='descricao_longa',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]