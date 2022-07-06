from django.shortcuts import render
from .models import PokemonCard
from .serializers import PokemonCardSerializer
from rest_framework import viewsets 

class PokemonCardViewset(viewsets.ModelViewSet):
    serializer_class = PokemonCardSerializer
    queryset = PokemonCard.objects.all()
