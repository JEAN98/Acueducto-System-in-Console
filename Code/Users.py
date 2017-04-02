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

        return self.__listUsers

    def addUser(self,id , password, admin, fullName, age, email):

        self.__listUsers.append({"id": id,
                                 "password": password,
                                 "administrator": admin,
                                 "fullName": fullName,
                                 "age": age,
                                 "email": email})