from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny

from api.lib.response import Response
from app.emails.send_otp import SendOTP
from app.emails.otp_verification import VerifyEmailVerify
# from app.emails.verify_otp import VerifyOTP


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
        email = request.data['email']
        otp_code = request.data['otp_code']
        verify_otp_user = VerifyOTP.call(otp_code=otp_code)
        if verify_otp_user.value:
            verify_email = VerifyEmailVerify.call(email=email)
            if verify_email.error:
                return Response(errors={"error": str(verify_email.error)})
            return Response(data=dict(verify_email.value))
        else:
            return Response(errors={"error": str(verify_otp_user.error)})


