from rest_framework.routers import DefaultRouter

from movies.api.viewsets.movies_views import FilmViewSet

router = DefaultRouter()

router.register(r'movies', FilmViewSet, basename='movies')
urlpatterns = router.urls
