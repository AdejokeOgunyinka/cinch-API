from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from api.lib.response import Response

class OtpsViewSet(ViewSet):
    @action(methods=['post'], detail=False)
    def send(self, request):
        data = dict(sample='Send OTP Email Action')
        return Response(data)

    @action(methods=['post'], detail=False)
    def verify(self, request):
        data = dict(sample='Verify OTP Action')
        return Response(data)
