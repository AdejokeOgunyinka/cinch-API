from app.action import Action
#from daos.user_dao import UsersDAO
from django.contrib.auth import  get_user_model
from db.models.user import User
from datetime import datetime
from django.utils import timezone
from db.serializers.user_serializer import UserSerializer

class VerifyOTP(Action):
    arguments = ['otp_code']

    def perform(self):
        user = get_user_model().objects.get(otp_code=self.otp_code)
        print(user.otp_code)
        print({"user": user.otp_code_expiry})
        expiry_time = user.otp_code_expiry
        if expiry_time > timezone.now():
            print("here")
            return user.otp_code
        else:
            print("time expired")
            raise Exception('Time Expired!!!')