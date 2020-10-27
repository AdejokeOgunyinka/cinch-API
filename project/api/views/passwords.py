from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, permission_classes


class PasswordsViewSet(ViewSet):
    @action(methods=['put'], detail=False, permission_classes=[IsAuthenticated])
    def change(self, request):
        return Response('Update User Password')

    @action(methods=['put'], detail=False)
    def reset(self, request):
        return Response('Reset User Password Action')
