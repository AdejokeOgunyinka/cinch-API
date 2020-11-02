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
        print({"otp": otp.value})

        if otp.value:
            # return Response(data=otp.value)
            return Response(data={"otp": otp.value})
        else:
            # return Response(errors=otp.error)
            return Response(errors={"error": str(otp.error)})

    @action(methods=['post'], detail=False)
    def verify(self, request):
        email = request.data['email']
        # this is get from the request that is coming in
        otp_code = request.data['otp_code']
        verify_otp_user = VerifyOTP.call(otp_code=otp_code)
        print({"verify_otp":verify_otp_user.value})
        if verify_otp_user.value:
            verify_email = VerifyEmailVerify.call(email=email)
            if verify_email.error:
                return Response(errors={"error": str(verify_email.error.value)})
            return Response(data=dict(verify_email.value))
        else:
            return Response(errors={"error": str(verify_otp_user.error)})
