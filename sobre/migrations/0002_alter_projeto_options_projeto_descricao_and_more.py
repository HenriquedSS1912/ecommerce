# Generated by Django 4.0.2 on 2022-02-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sobre', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projeto',
            options={'verbose_name': 'Projeto', 'verbose_name_plural': 'Projeto'},
        ),
        migrations.AddField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projeto',
            name='titulo',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
