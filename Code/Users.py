class Users:

    __listUsers = []

    def __init__(self):

        self.__listUsers.append({"id": "1",
                                 "administrator": False,
                                 "fullName": "Pedro Castellon",
                                 "age": 20,
                                 "email": "kma@pito.es",
                                 "password": "a"})

    def getList(self):
        'Return the list of users'

        return self.__listUsers

    def addUser(self,id , password, admin, fullName, age, email):
        """Add a user in the list users.
        You need identification, password, full name, age, email and know if he is an administrator."""

        self.__listUsers.append({"id": id,
                                 "password": password,
                                 "administrator": admin,
                                 "fullName": fullName,
                                 "age": age,
                                 "email": email})