from rest_framework.routers import DefaultRouter

from characters.api.viewsets.characters_views import CharacterViewSet

router = DefaultRouter()

router.register(r'characters', CharacterViewSet, basename='characters')

urlpatterns = router.urls
