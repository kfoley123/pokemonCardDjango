from django.db import models

# Create your models here.

class PokemonCard(models.Model):
    name = models.CharField(max_length=50)
    pokemonType = models.CharField(max_length=30)
    HP = models.CharField(max_length=3)

    def __str__(self):
        return self.name