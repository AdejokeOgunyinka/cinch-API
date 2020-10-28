from ..action import Action
# from .daos.users_dao.UsersDAO import update_password

# Define the action !!!

class UpdatePassword(Action):
    arguments = ['old_password','password','confirm_password', 'request']

    def perform(self):
        cur_user = self.request.user
        db_password = cur_user.password
        if self.old_password == db_password:
            if self.password == self.confirm_password:
                cur_user.save()
                return {'value': self.password}
            else:
                return {'error': "passwords don't match"}
        else:
            return {'error': "Incorrect Password"}





# class M_User(Action):
#     arguments = ['request']



# Call the action !!!
# Through result object returned, you have access to two attributes, namely
#   [value] The return value from the `perform` method
#   [error] Exception object representing error raised during action execution
#
# result = CreateArtist.call(name='John Doe', gender='Male')
# result.value
# result.error