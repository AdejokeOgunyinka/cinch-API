from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from api.lib.response import Response



class ArtistsViewSet(ViewSet):
    permission_classes = [AllowAny]

    @action(methods=['post'], detail=False, url_path='*')
    def create_profile(self, request):
        data = dict(sample='Create user profile')
        return Response(data)

