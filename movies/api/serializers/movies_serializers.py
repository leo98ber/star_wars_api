from rest_framework import serializers

from movies.models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class FilmJoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['name']
