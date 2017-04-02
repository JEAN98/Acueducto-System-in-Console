class Users:

    __listUsers = []

    def __init__(self):

        self.__listUsers.append({"id": "1",
                                 "administrator": False,
                                 "fullName": "Pedro Castellon",
                                 "edad": 20,
                                 "email": "kma@pito.es",
                                 "password": "a"})

    def getList(self):

        return self.__listUsers
