from django.shortcuts import render
from .models import PokemonCard, PokemonType
from .serializers import PokemonCardSerializer, PokemonTypeSerializer
from rest_framework import viewsets 

class PokemonCardViewset(viewsets.ModelViewSet):
    serializer_class = PokemonCardSerializer

    def get_queryset(self):
        queryset = PokemonCard.objects.all()
        pokemonType = self.request.query_params.get('pokemontype')
        if pokemonType is not None:
            queryset = queryset.filter(pokemonType=pokemonType)
        return queryset

class PokemonTypeViewset(viewsets.ModelViewSet):
    serializer_class = PokemonTypeSerializer

    def get_queryset(self):
        queryset = PokemonType.objects.all()
        return queryset