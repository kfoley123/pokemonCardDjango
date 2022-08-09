from rest_framework import serializers
from pokemoncard_api.models import PokemonCard, PokemonType, PokemonCardSet,  PokemonCollection



class PokemonTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PokemonType
        fields = '__all__'

class PokemonCardSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = PokemonCardSet
        fields = '__all__'


class PokemonCardReadSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = PokemonCard
        fields = ('id', 'pokedexIndex','name', 'HP', 'pokemonCardSet', 'type')
        depth =1
        

class PokemonCardWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PokemonCard
        fields = ('pokedexIndex','name', 'HP', 'pokemonCardSet', 'type')

class PokemonCollectionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonCollection
        fields = '__all__'
        depth = 2

class PokemonCollectionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonCollection
        fields = '__all__'
        