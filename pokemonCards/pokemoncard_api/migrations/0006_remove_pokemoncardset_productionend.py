# Generated by Django 4.0.6 on 2022-07-08 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemoncard_api', '0005_alter_pokemoncardset_icon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemoncardset',
            name='productionend',
        ),
    ]
