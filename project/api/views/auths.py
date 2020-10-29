from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny


from api.lib.response import Response
from app.auth.register import Register
from django.contrib.auth import authenticate
from rest_framework import status


class AuthsViewSet(ViewSet):
    permission_classes = [AllowAny]

    @action(methods=['post'], detail=False)
    def login(self, request):
        '''Generates an authtoken based on the email and password passed in as parameters.
        Enter email in the username field e.g: {'username': 'enter_email_here', 'password': 'your_password'}'''
        username = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False)
    def register(self, request):
        artist = Register.call(data=request.data)
        
        if artist.failed:
            return Response(
                errors=artist.error.value,
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            data=artist.value, 
            status=status.HTTP_201_CREATED
        )
