from app.action import Action
from daos.user_dao import UsersDAO
from datetime import datetime
from django.utils import timezone
from db.serializers.user_serializer import UserSerializer

class VerifyOTP(Action):
    arguments = ['otp_code']

    def perform(self):

        user = UsersDAO.fetch_user_by_otp_code(self.otp_code)
        expiry_time = user.otp_code_expiry
        if expiry_time > timezone.now():
            return user.otp_code
        else:
            raise Exception('Time Expired!!!')
