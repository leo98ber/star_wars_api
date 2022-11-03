from base.views import GeneralListApiView
from movies.api.serializers.movies_serializers import FilmSerializer


class FilmViewSet(GeneralListApiView):
    serializer_class = FilmSerializer
