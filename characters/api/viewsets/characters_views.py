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

    def get_by_pk(self):
        """ Make a query by id or primary key """
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    def create(self, request, **kwargs):
        """
        This method is used to create with a different serializer and send a custom message
        """
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Character created successfully!', 'content': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, **kwargs):
        """
        This method is used to update with a different serializer and send a custom message
        """
        if self.get_by_pk().exists():
            serializer = CharacterSerializer(instance=self.get_by_pk().get(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Object does not exist'}, status=status.HTTP_400_BAD_REQUEST)
