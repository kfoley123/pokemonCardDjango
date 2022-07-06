from pokemoncard_api.views import PokemonCardViewset
from rest_framework.routers import DefaultRouter
from pokemoncard_api import views


router = DefaultRouter()
router.register(r'pokemoncards', views.PokemonCardViewset, basename = 'pokemoncard')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemoncard_api/', include('pokemoncard_api.urls'))
]