from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, permission_classes


class ArtistsViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    @action(methods=['put'], detail=False, url_path='*')
    def update_profile(self, request):
        return Response('Update Artist Profile Details')
