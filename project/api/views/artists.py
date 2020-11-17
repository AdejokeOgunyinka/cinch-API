from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from app.artists.get_artist_profile import ArtistProfile
from api.lib.response import Response


class ArtistsViewSet(ViewSet):

    @action(methods=['post'], detail=False, url_path='*')
    def create_profile(self, request):
        data = dict(sample='Create user profile')
        return Response(data)

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
