from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from api.lib.response import Response


class AuthsViewSet(ViewSet):
    @action(methods=['post'], detail=False)
    def login(self, request):
        data = dict(sample='User Login Action')
        return Response(data)

    @action(methods=['post'], detail=False)
    def register(self, request):
        data = dict(sample='User Register Action')
        return Response(data)
