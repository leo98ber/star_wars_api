from rest_framework import viewsets

from base.views import GeneralListApiView
from characters.api.serializers.characters_serializers import CharacterSerializer
from characters.models import Character


class CharacterViewSet(GeneralListApiView):
    serializer_class = CharacterSerializer
