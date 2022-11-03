from rest_framework import viewsets, status, generics
from rest_framework import viewsets, filters

from base.views import GeneralListApiView, GeneralViewSet
from characters.api.serializers.characters_serializers import CharacterSerializer, ListCharacterSerializer
from characters.models import Character
from rest_framework.response import Response

from movies.api.serializers.movies_serializers import FilmSerializer


class CharacterViewSet(GeneralViewSet):
    serializer_class = CharacterSerializer


class FilterCharacterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ListCharacterSerializer
    queryset = serializer_class.Meta.model.objects.all()

    filter_backends = [filters.SearchFilter]

    search_fields = ['name', 'performer']
