#Do action here
from uploads.upload_interface import UploadInterface
from ..action import Action


class UploadImage(Action):
    arguments = ['data']

    def perform(self):
        url = UploadInterface.upload_image(self.data['image'])
        if url == 'Failed':
             self.fail(dict(invalid_format='Unaccepted Image Format'))

        return url

