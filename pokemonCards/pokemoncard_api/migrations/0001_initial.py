# Generated by Django 4.0.6 on 2022-07-06 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pokemonType', models.CharField(max_length=30)),
                ('HP', models.CharField(max_length=3)),
            ],
        ),
    ]