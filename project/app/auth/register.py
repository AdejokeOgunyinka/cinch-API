from db.serializers.user_serializer import UserSerializer
from django.contrib.auth import get_user_model

from app.action import Action
from db.models.artist import Artist


class Register(Action):
    arguments = ['data']

    def perform(self):
        user_serializer = UserSerializer(data=self.data)
        if not user_serializer.is_valid():
            self.fail(user_serializer.errors)

        otp = '123456'

        # Get all the Data
        email=self.data.get('email', '')
        username = self.data.get('username', '')
        phone_number = self.data.get('phone_number')
        password = self.data.get('password', '')
        firstname=self.data.get('first_name', '')
        lastname=self.data.get('last_name', '')

        if firstname and len(firstname) <= 2:
            self.fail(dict(firstname='firstname must be more than two characters'))

        if lastname and len(lastname) <= 2:
            self.fail(dict(lastname='lastname must be greater than two characters'))

        if username and len(username) <= 2:
            self.fail(dict(username='username must be greater than two characters'))

        user = get_user_model().objects.create(
            email=email,
            username = username,
            phone_number = phone_number,
            password = password,
            otp_code = otp
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
            otp=otp, username=username, first_name=firstname, 
            last_name=lastname, phone_number=phone_number
        )
        return return_data
