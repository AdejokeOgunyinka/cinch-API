from app.action import Action
from daos.user_dao import UsersDAO
from daos.artists_dao import ArtistsDAO


class CreateArtist(Action):
    arguments = ['email', 'username', 'firstname', 'lastname', 'phone_number', 'password', 'confirm_password']

    def perform(self):

        user = {
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "confirm_password": self.confirm_password
        }

        artist = {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "phone_number": self.phone_number
        }
        user_password = self.password
        user_confirm_password = self.confirm_password
        if user_password != user_confirm_password:
            raise Exception("Passwords do no match")

        user = UsersDAO.create_user(user)

        if not user:
            print("i am here")
            raise Exception("Error creating User")
        user_id = user["id"]
        print({"user": user})
        new_artist_data = {"firstname": self.firstname, "lastname": self.lastname, "phone_number": self.phone_number, "user_id": user_id}
        print(new_artist_data)
        artist_data = ArtistsDAO.create_artist(new_artist_data)
        print({"art": artist})


        if not artist:
            raise Exception("Error creating artist")

        return artist_data

