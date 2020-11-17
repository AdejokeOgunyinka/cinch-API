from db.serializers.artist_serializer import ArtistSerializer
from db.serializers.user_serializer import UpdateUserSerializer
from db.serializers.account_serializer import AccountSerializer
from app.action import Action
from db.models.artist import Artist
from db.models.user import User
from db.models.account import Account
from db.models.location import Location


class UpdateArtist(Action):
    arguments = ['data', 'user_id', 'bank_data']

    def perform(self):

        user_id = self.user_id
        artist = Artist.objects.get(user_id=self.user_id)
        account = Account.objects.get(artist_id=artist.id)

        user = User.objects.get(id=user_id)
        location = Location.objects.get(id=self.data['location_id'])

        data = dict(
            location_id=location.id,
            avatar_url=self.data["avatar_url"]
        )

        artist_serializer = ArtistSerializer(artist, data=data, partial=True)
        user_serializer = UpdateUserSerializer(user, data=self.data, partial=True)
        account_serializer = AccountSerializer(account, data=self.bank_data, partial=True)

        if user_serializer.is_valid():
            user_serializer.save()
        else:
            self.fail(user_serializer.errors)

        if artist_serializer.is_valid():
            artist_serializer.save()
        else:
            self.fail(artist_serializer.errors)

        if account_serializer.is_valid():
            account_serializer.save()
        else:
            self.fail(artist_serializer.errors)

        success_data = dict(
            account_number=self.bank_data['account_number'],
            bank_name=self.bank_data['bank_name'],
            location_id=self.data['location_id'],
            avatar_url=self.data['avatar_url'],
            phone_number=self.data['phone_number']
        )

        return success_data
