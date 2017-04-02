from Users import *

class LogInSystem:

    def __init__(self):

        self.__users = Users()

    def logIn(self, id, password):
        'Check ID and Password to login'

        for user in self.__users.getList():

            if user["id"] == id and user["password"] == password:

                return True, user["administrator"]

        return False, False

    def signUp(self,id , password, admin, fullName, age, email):

        if admin == "y":
            admin = True
        else:
            admin = False

        self.__users.addUser(id , password, admin, fullName, age, email)