from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from .models import PokemonCard, PokemonCollection, PokemonType, PokemonCardSet, User
from .serializers import *
from rest_framework import viewsets, status




class PokemonCardViewset(viewsets.ModelViewSet):

    def get_queryset(self):
        queryset = PokemonCard.objects.all()
        pokemonType = self.request.query_params.get('pokemontype')
        pokemonSet = self.request.query_params.get('pokemonset')
        if pokemonType is not None:
            queryset = queryset.filter(type=pokemonType)
        if pokemonSet is not None:
            queryset = queryset.filter(pokemonCardSet=pokemonSet)
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

        pokemonType = self.request.query_params.get('pokemontype')
        pokemonSet = self.request.query_params.get('pokemonset')
        user = self.request.query_params.get('user')

        if pokemonType is not None:
            queryset = queryset.filter(collectedCard__type=pokemonType)
        if pokemonSet is not None:
            queryset = queryset.filter(collectedCard__pokemonCardSet=pokemonSet)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset
    
    def get_serializer_class(self):
        method = self.request.method
        if method == "PUT" or method == "POST":
            return PokemonCollectionWriteSerializer
        else: 
            return PokemonCollectionReadSerializer

class UserViewset(viewsets.ModelViewSet):

    def get_serializer_class(self):
        method = self.request.method
        if method == "POST":
            return UserWriteSerializer
        else:
            return UserReadSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset 

class LogInViewset(viewsets.ModelViewSet):
    serializer_class = LogInSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def update(self, request, *args, **kwargs):
        
        password = request.data.get("password")
        try:
            userInDB = User.objects.get(password=password)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if userInDB:
            serializer=LogInSerializer(userInDB, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else: return Response(status=status.HTTP_404_NOT_FOUND)
     
        
