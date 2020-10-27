from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, permission_classes
from api.lib.response import Response


class PasswordsViewSet(ViewSet):
    @action(methods=['put'], detail=False, permission_classes=[IsAuthenticated])
    def change(self, request):
        return Response.create(dict(sample='Update User Password'))

    @action(methods=['put'], detail=False)
    def reset(self, request):
        return Response.create(dict(sample='Reset User Password Action'))