# Generated by Django 4.1.7 on 2023-05-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_remove_musica_participa_musica_participa_banda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='musico',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]