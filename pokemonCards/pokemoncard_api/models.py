from django.db import models

# Create your models here.

class PokemonCard(models.Model):
    name = models.CharField(max_length=50)
    pokemonType = models.CharField(max_length=30)
    HP = models.CharField(max_length=3)
    pokedexIndex = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class PokemonType(models.Model):
    pokemonType = models.CharField(max_length=30)

    def __str__(self):
        return self.pokemonType

class PokemonCardSet(models.Model):
    name = models.CharField(max_length=50)
    productionstart = models.DateField()
    icon = models.CharField(max_length=2048)

    def __str__(self):
        return self.name

