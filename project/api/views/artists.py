from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from api.lib.response import Response
from app.artists.create_artist import CreateArtist


class ArtistsViewSet(ViewSet):
    permission_classes = [AllowAny]

    @action(methods=['post'], detail=False, url_path='*')
    def create_profile(self, request):
        artist = CreateArtist.call(data=request.POST)
        
        if artist.failed:
            return Response(
                errors=artist.error.value,
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            data=artist.value, 
            status=status.HTTP_201_CREATED
        )

