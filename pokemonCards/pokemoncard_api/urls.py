from django.contrib import admin 
from django.urls import path,include
from rest_framework import routers 
from pokemoncard_api import views

router = routers.DefaultRouter()
router.register(r'pokemoncards', views.PokemonCardViewset, basename = 'pokemoncard')
router.register(r'pokemontypes', views.PokemonTypeViewset, basename ='pokemontype')
router.register(r'pokemoncardsets', views.PokemonCardSetViewset, basename = 'pokemoncardset')
urlpatterns = [
    path('', include(router.urls)),
]

