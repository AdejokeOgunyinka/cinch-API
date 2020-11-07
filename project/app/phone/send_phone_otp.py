from datetime import timedelta
from django.conf import settings
from django.utils import timezone

from twilio.rest import Client

from app.action import Action
from db.models.user import User
from app.emails.send_otp import SendOTP
from lib.generate_otp import generate_otp
from db.serializers.phone_number_serializer import PhoneNumberSerializer


class PhoneOtpAction(Action):
    arguments = ['data', 'otp']

    def perform(self):
        email_exist = 'email' in self.data and self.data['email']

        if not email_exist:
            self.fail(dict(invalid_email='Please provide an email'))

        user = self.get_queryset(self.data['email']) #gets instance of user

        if not user:
            self.fail(dict(invalid_email='Please provide a valid email'))

        phone_number_valid = PhoneNumberSerializer(data=self.data)
        if not phone_number_valid.is_valid():
            self.fail(phone_number_valid.errors)

        phone_number = self.data['phone_number']
        otp = self.otp
        if otp is None:
            otp = generate_otp()

        user.otp_code=otp #accesses otp_code attribute
        user.phone_number = self.data['phone_number']
        expiry = timezone.now() + timedelta(minutes=10)
        user.otp_code_expiry = expiry
        user.email_verified = False
        user.save()

        email = self.data['email']

        # send otp to email
        SendOTP.call(email=email, otp=otp) 

        # Send Otp to phone 
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message_to_broadcast = (f'Your Cinch Verification code is {otp}')
        client.messages.create(to=phone_number,
                               from_=settings.TWILIO_NUMBER,
                               body=message_to_broadcast)
        return dict(otp=otp)

    def get_queryset(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return False
