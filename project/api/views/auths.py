from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from api.lib.response import Response


class AuthsViewSet(ViewSet):
    @action(methods=['post'], detail=False)
    def login(self, request):
        return Response.create(dict(sample='User Login Action'))

    @action(methods=['post'], detail=False)
    def register(self, request):
        return Response.create(dict(sample='User Register Action'))
