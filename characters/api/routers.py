from rest_framework.routers import DefaultRouter

from characters.api.viewsets.characters_views import CharacterViewSet, FilterCharacterViewSet

router = DefaultRouter()

router.register(r'characters', CharacterViewSet, basename='characters')
router.register(r'filter_characters', FilterCharacterViewSet, basename='filter_characters')
urlpatterns = router.urls
