from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class AuthsViewSet(ViewSet):
    @action(methods=['post'], detail=False)
    def login(self, request):
        return Response('User Login Action')

    @action(methods=['post'], detail=False)
    def register(self, request):
        return Response('User Register Action')
