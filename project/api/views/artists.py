from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, permission_classes
from api.lib.response import Response


class ArtistsViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    @action(methods=['put'], detail=False, url_path='*')
    def update_profile(self, request):
        data = dict(sample='Update Artist Profile Details')
        return Response(data)
