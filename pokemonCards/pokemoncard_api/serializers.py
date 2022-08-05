from rest_framework import serializers
from pokemoncard_api.models import PokemonCard, PokemonType, PokemonCardSet



class PokemonTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PokemonType
        fields = '__all__'

class PokemonCardSetSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = PokemonCardSet
        fields = ('name', 'productionstart', 'icon') 


class PokemonCardSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    pokemonCardSet=PokemonCardSetSerializer()
    type=serializers.SlugRelatedField(many=False, read_only=True, slug_field='pokemonType')

    
    class Meta:
        model = PokemonCard
        fields = ('id', 'pokedexIndex','name', 'pokemonType', 'HP', 'pokemonCardSet', 'type')