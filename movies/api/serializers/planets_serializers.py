from rest_framework import serializers

from movies.models import Planet


class PlanetJoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'
