from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class PasswordSerializer(serializers.Serializer):
    """

    """
    old_password = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate_old_password(self, value):
        """

        """
        user = self.context['user']
        if not user.check_password(value):
            raise serializers.ValidationError('Old password is incorrect. Please enter it again.')
        return value

    def validate(self, data):
        """

        """
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirm_password': "The two password fields didn't match."})
        validate_password(data['password'], self.context['user'])
        return data

    def save(self, **kwargs):
        """

        """
        password = self.validated_data['password']
        user = self.context['user']
        user.set_password(password)
        user.save()
        print({"user_detail": user})
        return user
