from rest_framework import serializers

from movies.models import Film


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'name': instance.name
        }
