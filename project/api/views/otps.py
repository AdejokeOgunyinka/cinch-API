from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework import status
from api.lib.response import Response
from app.emails.send_otp import SendOTP



class OtpsViewSet(ViewSet):

    @action(methods=['post'], detail=False)
    def send(self, request):

        email = request.data['email']
        otp = SendOTP.call(email=email)

        if otp.value:
            return Response(data={"otp": otp.value}, status=status.HTTP_201_CREATED)
        else:
            return Response(errors={"error": otp.error.value}, status=status.HTTP_400_BAD_REQUEST)