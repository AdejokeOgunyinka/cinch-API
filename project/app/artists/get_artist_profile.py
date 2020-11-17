from ..action import Action
from db.models.artist import Artist
from db.models.account import Account
from db.models.user import User
from db.models.location import Location
from db.serializers.artist_serializer import ArtistSerializer
from db.serializers.account_serializer import AccountSerializer
from db.serializers.user_serializer import UserSerializer
from db.serializers.location_serializer import LocationSerializer


class ArtistProfile(Action):
    arguments = ['user']

    def perform(self):
        user = self.user
        # print(user.id)

        artist_info = Artist.objects.get(user_id=user.id)

        user_info = User.objects.get(id=user.id)
        print(artist_info.location_id,'==============')

        location_info = Location.objects.get(id=artist_info.location_id)

        serialize_artist = ArtistSerializer(artist_info)
        # print(serialize_artist.data, '=============')
        # artist_id = serialize_artist.data['id']
        # print(artist_id)

        # account_info = Account.objects.get(artist_id=artist_id)
        # print(account_info, '========')

        serialize_user = UserSerializer(user_info)
        print(serialize_user.data)
        print('============')


        # serialize_account = AccountSerializer(account_info)
        serialize_location = LocationSerializer(location_info)
        print(serialize_location.data)

        return dict(artist_information=serialize_artist.data)
