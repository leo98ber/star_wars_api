from rest_framework import serializers

from movies.models import Film, Planet


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ['name', 'location']


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class FilmJoinSerializer(serializers.ModelSerializer):
    planets = PlanetSerializer(many=True)

    class Meta:
        model = Film
        fields = ['name', 'open_text', 'productor', 'director', 'planets']
