from rest_framework import viewsets
from django.conf import settings
from db.models.user import User
from twilio.rest import Client
from lib.generate_otp import generate_otp
from app.action import Action
from db.serializers.phone_number_serializer import PhoneNumberSerializer

class PhoneOtpAction(Action):
    arguments = ['data']

    # check if the email exist
    #     if email not exist and not in db return error message
    #     check phone number valid
    #      if not valid returns error
    #      generate token
    #      save token to db against the user row

    #    send sms to user

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


        otp = self.data['data']

        if otp is None:
            get_otp = generate_otp()
            otp = get_otp

        user.otp_code=otp #accesses otp_code attribute
        user.phone_number = self.data['phone_number']
        user.save()

        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        message_to_broadcast = (f'Your Cinch Verification code is {otp}')

        client.messages.create(to=self.data['phone_number'],
                               from_=settings.TWILIO_NUMBER,
                               body=message_to_broadcast)
        return {'otp': otp}

    def get_queryset(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return False

    # def broadcast_sms(self, request):
    #     phone_number = request.data.get("phone_number")
    #     user = self.get_queryset(phone_number)
    #
    #     if not user:
    #         return Response({"message":"user does not exist"}, status=status.HTTP_404_NOT_FOUND)
    #
    #     if phone_number:
    #         otp = generate_otp()
    #         client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    #         message_to_broadcast = (f'Welcome to Cinch, here is your code{otp}')
    #         client.messages.create(to=phone_number,
    #                                from_=settings.TWILIO_NUMBER,
    #                                body=message_to_broadcast)
    #     print(otp)
    #     return otp