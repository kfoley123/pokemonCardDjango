# Generated by Django 4.0.6 on 2022-08-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemoncard_api', '0011_alter_pokemoncollection_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemoncard',
            name='image',
            field=models.URLField(default=1),
        ),
    ]
