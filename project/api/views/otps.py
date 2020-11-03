from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny

from api.lib.response import Response
from app.emails.send_otp import SendOTP
from app.emails.otp_verification import VerifyEmailVerify


class OtpsViewSet(ViewSet):
    permission_classes = [AllowAny]
    @action(methods=['post'], detail=False)
    def send(self, request):
        email = request.data.get('email', '')
        otp = SendOTP.call(email=email)

        if otp.value:
            return Response(data={"otp": otp.value}, status=status.HTTP_201_CREATED)
        else:
            return Response(errors={"error": otp.error.value}, status=status.HTTP_400_BAD_REQUEST)
            
    @action(methods=['post'], detail=False)
    def verify(self, request):
        email = request.data.get('email', '')
        otp_code = request.data.get('otp_code', '')

        verify_email = VerifyEmailVerify.call(email=email, otp=otp_code)

        if verify_email.failed:
            return Response(
                errors=verify_email.error.value,
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(data=verify_email.value)


