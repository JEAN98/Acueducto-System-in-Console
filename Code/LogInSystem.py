from Users import *
from User import *

class LogInSystem:
    "System of log in and sign up"

    __state = False
    __user = User('', '', False, '', '', '')

    def __init__(self):

        self.__users = Users()


    def getUser(self):

        return self.__user

    def getState(self):

        return self.__state

    def logIn(self, id, password):
        'Check ID and Password to login'

        for user in self.__users.getList():

            if user.getId() == id and user.getPassword() == password:

                self.__user = user
                self.__state = True
                break

    def signUp(self,id , password, admin, fullName, age, email):
        """Create a user in the users.
        You need identification, password, full name, age, email and know if he is an administrator."""

        if admin == "y":
            admin = True
        else:
            admin = False

        self.__users.addUser(id , password, admin, fullName, age, email)