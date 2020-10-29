from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from api.lib.response import Response
from app.emails.send_otp import SendOTP
from app.emails.verify_otp import VerifyOTP
from app.emails.email_template import email_template
from app.emails.otp_verification import VerifyEmailVerify



class OtpsViewSet(ViewSet):

    @action(methods=['post'], detail=False)
    def send(self, request):

        email = request.data['email']
        otp = SendOTP.call(email=email)

        if otp.value:
            return Response(data={"otp": otp.value})
        else:
            return Response(errors={"error": str(otp.error)})
