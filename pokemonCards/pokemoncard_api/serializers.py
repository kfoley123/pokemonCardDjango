from rest_framework import serializers
from pokemoncard_api.models import PokemonCard, PokemonType, PokemonCardSet

class PokemonCardSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = PokemonCard
        fields = ('id', 'pokedexIndex','name', 'pokemonType', 'HP')

class PokemonTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PokemonType
        fields = '__all__'

class PokemonCardSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = PokemonCardSet
        fields = ('name', 'productionstart', 'icon') 