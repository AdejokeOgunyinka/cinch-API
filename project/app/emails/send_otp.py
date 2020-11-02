from app.action import Action
from django.contrib.auth import get_user_model
from lib.generate_otp import generate_otp
from datetime import datetime, timedelta
from django.utils import timezone

class SendOTP(Action):
    arguments = ['email']

    def perform(self):
        
        otp = generate_otp()
        user = get_user_model().objects.get(email=self.email)
        user.otp_code = otp
        expiry = timezone.now() + timedelta(minutes=10)
        user.otp_code_expiry = expiry
        user.email_verified = False
        user.save()

        otp_value = user.otp_code
        email = self.email
        email_subject = 'Email Verification OTP'
        username = user.username

        email_body = f'Hi {username} Here is the OTP Code to validate your email. \n OTP Code:{otp_value}'
        email_template(email_subject, email, email_body)

        return otp_value
