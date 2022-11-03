from rest_framework import viewsets, filters, status
from rest_framework.decorators import action

from base.views import GeneralViewSet
from characters.api.serializers.characters_serializers import CharacterSerializer, ListCharacterSerializer
from rest_framework.response import Response


class CharacterViewSet(GeneralViewSet):
    serializer_class = CharacterSerializer


class FilterCharacterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ListCharacterSerializer
    queryset = serializer_class.Meta.model.objects.all()

    filter_backends = [filters.SearchFilter]

    search_fields = ['name', 'performer']

    @action(detail=False, methods=['post'])
    def create_character(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Character created succesffully!'}, status=status.HTTP_201_CREATED)
        return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
