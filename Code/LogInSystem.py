from Users import *

class LogInSystem:
    "System of log in and sign up"

    def __init__(self):

        self.__users = Users()

    def logIn(self, id, password):
        'Check ID and Password to login'

        for user in self.__users.getList():

            if user.getId() == id and user.getPassword() == password:

                return True, user.getAdministator()

        return False, False

    def signUp(self,id , password, admin, fullName, age, email):
        """Create a user in the users.
        You need identification, password, full name, age, email and know if he is an administrator."""

        if admin == "y":
            admin = True
        else:
            admin = False

        self.__users.addUser(id , password, admin, fullName, age, email)