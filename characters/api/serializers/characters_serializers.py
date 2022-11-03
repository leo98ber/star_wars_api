from rest_framework import serializers

from characters.models import Character
from movies.api.serializers.movies_serializers import FilmSerializer, FilmJoinSerializer
from movies.models import Film


class ListCharacterSerializer(serializers.ModelSerializer):
    movies = FilmJoinSerializer(Film, many=True, read_only=True)

    class Meta:
        model = Character
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
