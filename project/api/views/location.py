from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from api.lib.response import Response
from app.locations.location_action import GetLocation


class LocationViewset(ViewSet):
    permission_classes = [AllowAny]

    @action(methods=['get'], detail=False, url_path='*')
    def get_location(self, request):
        result = GetLocation.call()
        return Response(result.value, status=status.HTTP_200_OK)
