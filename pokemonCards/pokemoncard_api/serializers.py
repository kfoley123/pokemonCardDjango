from rest_framework import serializers
from pokemoncard_api.models import PokemonCard, PokemonType, PokemonCardSet,  PokemonCollection, User



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
        fields = ('id','image', 'pokedexIndex','name', 'HP', 'pokemonCardSet', 'type')
        depth =1
        

class PokemonCardWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PokemonCard
        fields = ('pokedexIndex','name', 'image', 'HP', 'pokemonCardSet', 'type')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','profilePic'  )

class LogInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'loggedIn', 'profilePic')

class PokemonCollectionReadSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    collectedCard = PokemonCardReadSerializer()

    class Meta:
        model = PokemonCollection
        fields = ('id', 'user', 'collectedCard', 'quantity')
        

class PokemonCollectionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonCollection
        fields = '__all__'
        