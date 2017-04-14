from Code.User import User

class Users:

    __listUsers = []

    def __init__(self):

        self.__listUsers.append(User('1' , 'a', True, 'Pedro Castellon', 20, 'kma@pito.es'))
        self.__listUsers.append(User('2' , 'a', False, 'Juan Caballom', 30, 'kma@pito.es'))

    def getList(self):
        'Return the list of users'

        return self.__listUsers



    def addUser(self,id , password, admin, fullName, age, email):
        """Add a user in the list users.
        You need identification, password, full name, age, email and know if he is an administrator."""

        user = User(id , password, admin, fullName, age, email)
        self.__listUsers.append(user)