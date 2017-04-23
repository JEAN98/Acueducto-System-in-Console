from User import User

class Users:

    __listUsers = []

    def __init__(self):

        self.__listUsers.append(User('01' , '1', True, 'Kenet Acuña', 22, 'kmal.kenneth@gmail.com'))
        self.__listUsers.append(User('2', 'a', False, 'Juan Caballom', 30, 'kma@pito.es'))
        self.__listUsers.append(User("206950338","1992",True,"Steve Araya Solorzano",25,"stevenaraya.24@gmail.com"))
        self.__listUsers.append(User("201106154", "21", False, "Adelso Solorzano", 40, "adelso.24@gmail.com"))

    def getList(self):
        'Return the list of users'

        return self.__listUsers



    def addUser(self,id , password, admin, fullName, age, email):
        """Add a user in the list users.
        You need identification, password, full name, age, email and know if he is an administrator."""

        user = User(id , password, admin, fullName, age, email)
        self.__listUsers.append(user)