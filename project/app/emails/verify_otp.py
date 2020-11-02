from app.action import Action
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils import timezone
from db.serializers.user_serializer import UserSerializer

class VerifyOTP(Action):
    arguments = ['otp_code']

    def perform(self):


        user = get_user_model().objects.get(otp_code=self.otp_code)
        expiry_time = user.otp_code_expiry
        if expiry_time > timezone.now():
            return user.otp_code
        else:
            raise Exception('Time Expired!!!')
