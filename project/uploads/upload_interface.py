import cloudinary.uploader
from lib.generate_string import get_random_string


class UploadInterface:
    audio_extensions = ['mp3','aac', 'aiff', 'amr', 'flac', 'm4a', 'ogg', 'opus', 'wav']
    image_extensions =['jpg', 'jpe', 'jpeg', 'png', 'gif', 'svg', 'webp']

    @classmethod
    def upload_audio(cls, song):
        song_details = song.name.split(".")

        song_ext = song_details[-1]
        if song_ext not in cls.audio_extensions:
            return False

        song_name = get_random_string()
        upload_data = cloudinary.uploader.upload_large(song, public_id=f'Songs/{song_name}', resource_type="video")

        url = upload_data.get('url')
        return dict(url=url)

    @classmethod
    def upload_image(cls, image):

        image_details = image.name.split(".")
        image_ext = image_details[-1]
        if image_ext not in cls.image_extensions:
            return False

        img_name = get_random_string()
        upload_data = cloudinary.uploader.upload_large(image, public_id=f'Images/{img_name}', resource_type="image")

        url = upload_data.get('url')
        return dict(url=url)
