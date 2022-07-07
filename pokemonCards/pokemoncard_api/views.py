from django.shortcuts import render
from .models import PokemonCard
from .serializers import PokemonCardSerializer
from rest_framework import viewsets 

class PokemonCardViewset(viewsets.ModelViewSet):
    serializer_class = PokemonCardSerializer

    def get_queryset(self):
        queryset = PokemonCard.objects.all()
        pokemonType = self.request.query_params.get('pokemontype')
        if pokemonType is not None:
            queryset = queryset.filter(pokemonType=pokemonType)
        return queryset
