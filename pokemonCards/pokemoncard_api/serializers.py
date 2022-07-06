from rest_framework import serializers
from pokemoncard_api.models import PokemonCard

class PokemonCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonCard
        fields = ('name', 'pokemonType', 'HP')