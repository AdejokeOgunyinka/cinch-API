from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.authtoken.models import Token
from app.artists.get_artist_profile import ArtistProfile
from api.lib.response import Response


class ArtistProfileViewSet(ViewSet):
    @action(methods=['get'], detail=False, permission_classes=[IsAuthenticated], url_path='*')
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
