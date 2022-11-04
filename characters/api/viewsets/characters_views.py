from rest_framework import filters, status

from base.views import GeneralViewSet
from characters.api.serializers.characters_serializers import CharacterSerializer, ListCharacterSerializer
from rest_framework.response import Response


class CharacterViewSet(GeneralViewSet):

    """
    This class is the base of the CRUD to create characters and also contains the option to filter
    """
    serializer_class = ListCharacterSerializer
    queryset = serializer_class.Meta.model.objects.all()

    filter_backends = [filters.SearchFilter]

    search_fields = ['name', 'performer']

    def create(self, request, **kwargs):
        """
        This method is used to create with a different serializer
        """
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Character created successfully!', 'content': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
