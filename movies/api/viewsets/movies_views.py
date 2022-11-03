from base.views import GeneralViewSet
from movies.api.serializers.movies_serializers import FilmSerializer


class FilmViewSet(GeneralViewSet):
    serializer_class = FilmSerializer
