from django.shortcuts import render
from .models import PokemonCard, PokemonCollection, PokemonType, PokemonCardSet
from .serializers import PokemonCardReadSerializer,PokemonCardWriteSerializer, PokemonCollectionReadSerializer, PokemonCollectionWriteSerializer, PokemonTypeSerializer, PokemonCardSetSerializer
from rest_framework import viewsets 


class PokemonCardViewset(viewsets.ModelViewSet):
    # serializer_class = PokemonCardReadSerializer

    def get_queryset(self):
        queryset = PokemonCard.objects.all()
        pokemonType = self.request.query_params.get('pokemontype')
        if pokemonType is not None:
            queryset = queryset.filter(pokemonType=pokemonType)
        return queryset

    def get_serializer_class(self):
        method = self.request.method
        if method == "PUT" or method == "POST":
            return PokemonCardWriteSerializer
        else: 
            return PokemonCardReadSerializer

class PokemonTypeViewset(viewsets.ModelViewSet):
    serializer_class = PokemonTypeSerializer

    def get_queryset(self):
        queryset = PokemonType.objects.all()
        return queryset

class PokemonCardSetViewset(viewsets.ModelViewSet):
    serializer_class = PokemonCardSetSerializer

    def get_queryset(self):
        queryset = PokemonCardSet.objects.all()
        return queryset

class PokemonCollectionViewset(viewsets.ModelViewSet):
   

    def get_queryset(self):
        queryset = PokemonCollection.objects.all()
        return queryset
    
    def get_serializer_class(self):
        method = self.request.method
        if method == "PUT" or method == "POST":
            return PokemonCollectionWriteSerializer
        else: 
            return PokemonCollectionReadSerializer