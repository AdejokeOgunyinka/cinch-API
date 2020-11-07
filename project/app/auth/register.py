from db.serializers.user_serializer import UserSerializer
from django.contrib.auth import get_user_model

from app.action import Action
from db.models.artist import Artist
from app.emails.send_otp import SendOTP
from ..validations.validate_artist import RegisterArtistValidation


class Register(Action):
    arguments = ['data']

    def perform(self):
        user_serializer = UserSerializer(data=self.data)
        if not user_serializer.is_valid():
            self.fail(user_serializer.errors)

        # Get all the Data
        email=self.data.get('email', '')
        username = self.data.get('username', '')
        phone_number = self.data.get('phone_number')
        password = self.data.get('password', '')
        firstname=self.data.get('first_name', '')
        lastname=self.data.get('last_name', '')

        # Validate fields
        valid_artist = RegisterArtistValidation.validate_artist(self.data, self.fail)
        if not valid_artist: return valid_artist

        user = get_user_model().objects.create(
            email=email,
            username = username,
            phone_number = phone_number,
            password = password,
        )
        user.set_password(password)

        artist = Artist.objects.create(
            user_id = user,
            firstname=firstname,
            lastname=lastname,
        )
        
        # save user to db
        user.save()

        # save artist to db
        artist.save()

        return_data = dict(
            email=email, username=username, first_name=firstname, 
            last_name=lastname, phone_number=phone_number
        )
        return return_data
