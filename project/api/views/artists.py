from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from ..lib.response import Response
from rest_framework import status
from app.artists.create_artist import CreateArtist


class ArtistsViewSet(ViewSet):
    permission_classes = [AllowAny]

    @action(methods=['post'], detail=False, url_path='*')
    def create_profile(self, request):
        data = request.data
        artist = CreateArtist.call(email=data["email"], username=data["username"], firstname=data["firstname"], lastname=data["lastname"], phone_number=data["phone_number"], password=data["password"], confirm_password=data["confirm_password"])
        if artist.error:
            return Response(errors={"error": str(artist.error), "status": status.HTTP_400_BAD_REQUEST})
        print(type(artist.value))
        return Response(data = dict(artist.value))

    @action(methods=['put'], detail=False, url_path='*')
    def update_profile(self, request):
        data = dict(sample='Update Artist Profile Details')
        return Response(data)
