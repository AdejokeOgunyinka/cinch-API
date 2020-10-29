from rest_framework.serializers import ModelSerializer
from ..models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['created_at', 'updated_at']  # update this as necessary
