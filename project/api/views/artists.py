from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from app.artists.get_artist_profile import ArtistProfile
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from app.artists.update_artist import UpdateArtist
from api.lib.response import Response
from rest_framework.authtoken.models import Token
from payment.account_verification import AccountVerification

class ArtistsViewSet(ViewSet):

    @action(methods=['post'], permission_classes=[AllowAny], detail=False, url_path='*')
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
    @action(methods=['put'], detail=False, permission_classes=[IsAuthenticated], url_path='update')
    def update_profile(self, request):

        authorization_token = request.headers.get('Authorization')
        token = authorization_token.split(' ')[1]
        user_id = Token.objects.get(key=token).user_id
        account_details = AccountVerification.call(data=request.data)

        if account_details.failed:
            return Response(errors=account_details.error.value, status=status.HTTP_400_BAD_REQUEST)

        res = account_details.value
        account_data = res.get('data')

        bank_data = dict(
            account_number=account_data.get('account_number'),
            account_name=account_data.get('account_name'),
            bank_name=request.data.get('bank_name'),
            bank_code=request.data.get('bank_code')
        )

        artist = UpdateArtist.call(data=request.data, user_id=user_id, bank_data=bank_data)

        if artist.failed:
            return Response(errors=artist.error.value, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=artist.value, status=status.HTTP_200_OK)
