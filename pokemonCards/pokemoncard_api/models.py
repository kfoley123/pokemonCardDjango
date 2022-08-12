from django.db import models

# Create your models here.

class PokemonCard(models.Model):
    name = models.CharField(max_length=50)
    HP = models.CharField(max_length=3)
    pokedexIndex = models.IntegerField(default=0)
    pokemonCardSet = models.ForeignKey("PokemonCardSet", on_delete=models.CASCADE, default=1)
    type = models.ForeignKey("PokemonType", on_delete=models.CASCADE, default=1)
    image=models.URLField(default=1)

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

class PokemonCollection(models.Model):
    user = models.CharField(max_length=100)
    collectedCard = models.ForeignKey("PokemonCard", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.user

