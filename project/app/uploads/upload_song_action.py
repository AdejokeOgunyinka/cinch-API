from uploads.upload_interface import UploadInterface
from app.action import Action
from db.models.artist import Artist
from db.serializers.song_serializer import SongSerializer

class UploadSong(Action):
    arguments = ['data', 'user_email']

    def perform(self):
        artist = Artist.objects.get(user_id=self.user_email).id

        title = self.data.get('title','')

        new_data = dict(
            url=self.data.get('song_url'),
            cover_art_url=self.data.get('image_url'),
            title=title,
            artist_id=artist
        )


        song_serializer = SongSerializer(data=new_data)


        if not song_serializer.is_valid():
            self.fail(song_serializer.errors)

        song_serializer.save()

        return new_data

