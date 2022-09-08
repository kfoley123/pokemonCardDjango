from django.contrib import admin 
from django.urls import path,include
from rest_framework import routers 
from pokemoncard_api import views

router = routers.DefaultRouter()
router.register(r'pokemoncards', views.PokemonCardViewset, basename = 'pokemoncard')
router.register(r'pokemontypes', views.PokemonTypeViewset, basename ='pokemontype')
router.register(r'pokemoncardsets', views.PokemonCardSetViewset, basename = 'pokemoncardset')
router.register(r'pokemoncollections', views.PokemonCollectionViewset, basename = 'pokemoncollection')
router.register(r'users', views.UserViewset, basename = 'user')
router.register(r'login', views.LogInViewset, basename = 'login')
urlpatterns = [
    path('', include(router.urls)),
]

