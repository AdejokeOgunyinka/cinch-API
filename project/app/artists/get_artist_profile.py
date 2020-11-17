from ..action import Action
from db.models.artist import Artist
from db.models.user import User
from db.models.location import Location
from db.serializers.artist_serializer import ArtistSerializer
from db.serializers.user_serializer import UserSerializer
from db.serializers.location_serializer import LocationSerializer


class ArtistProfile(Action):
    arguments = ['user']

    def perform(self):
        user = self.user
        artist_info = Artist.objects.get(user_id=user.id)
        user_info = User.objects.get(id=user.id)

        location_id = '+' + str(artist_info.location_id_id)
        location_info = Location.objects.get(country_code=location_id)

        serialize_artist = ArtistSerializer(artist_info)
        serialize_user = UserSerializer(user_info)
        serialize_location = LocationSerializer(location_info)

        artist_information = {
            'email': serialize_user.data['email'],
            'phone_number': serialize_user.data['phone_number'],
            'username': serialize_user.data['username'],
            'location': serialize_location.data['country'],
            'avatar_url': serialize_artist.data['avatar_url'],
            'first_name': serialize_artist.data['firstname'],
            'last_name': serialize_artist.data['lastname']
        }

        return dict(artist_profile=artist_information)
