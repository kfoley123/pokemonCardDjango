from django.contrib import admin
from .models import PokemonCard

class PokemonCardAdmin(admin.ModelAdmin):
    list = ("name", "pokemonType", "HP")
    admin.site.register(PokemonCard)

