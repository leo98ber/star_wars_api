from rest_framework.routers import DefaultRouter

from movies.api.viewsets.movies_views import FilmViewSet
from movies.api.viewsets.planets_views import PlanetViewSet

router = DefaultRouter()

router.register(r'movies', FilmViewSet, basename='movies')
router.register(r'planets', PlanetViewSet, basename='planets')

urlpatterns = router.urls
