from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from api.lib.response import Response

class OtpsViewSet(ViewSet):
    @action(methods=['post'], detail=False)
    def send(self, request):
        return Response.create(dict(sample='Send OTP Email Action'))

    @action(methods=['post'], detail=False)
    def verify(self, request):
        return Response.create(dict(sample='Verify OTP Action'))
