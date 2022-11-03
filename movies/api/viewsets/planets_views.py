from base.views import GeneralViewSet
from movies.api.serializers.planets_serializers import PlanetJoinSerializer


class PlanetViewSet(GeneralViewSet):
    serializer_class = PlanetJoinSerializer
