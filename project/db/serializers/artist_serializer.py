from rest_framework.serializers import ModelSerializer
from ..models.artist import Artist


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        exclude = ['created_at', 'updated_at', 'avatar_url']  # update this as necessary
