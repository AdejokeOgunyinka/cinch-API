from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from app.artists.get_artist_profile import ArtistProfile
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from app.artists.update_artist import UpdateArtist
from api.lib.response import Response

class ArtistsViewSet(ViewSet):
    
    @action(methods=['get'], detail=False, url_path='detail')
    def get_artist(self, request):
        """
        This method updates the user's password and returns an appropriate response.
        """
        user = request.user
        result = ArtistProfile.call(user=user)

        if result.failed:
            return Response(
                errors=result.error.value,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(data=result.value, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=False, permission_classes=[IsAuthenticated], url_path='update')
    def update_profile(self, request):
        request_email = request.user
        artist = UpdateArtist.call(data=request.data, user_email=request_email)

        if artist.failed:
            return Response(errors=artist.error.value, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=artist.value, status=status.HTTP_200_OK)
