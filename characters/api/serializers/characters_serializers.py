from rest_framework import serializers

from characters.models import Character
from movies.api.serializers.movies_serializers import FilmSerializer
from movies.models import Film


class CharacterSerializer(serializers.ModelSerializer):
    movies = FilmSerializer(Film, many=True)

    class Meta:
        model = Character
        fields = '__all__'
