class User:

    def __init__(self, id, password, administrator, fullname, age, email):

        self.__id = id
        self.__password = password
        self.__administartor = administrator
        self.__fullname = fullname
        self.__age = age
        self.__email = email

    def getId(self):
        """Gets the property: ID"""

        return self.__id

    def getPassword(self):
        """Gets the property: Password"""

        return self.__password

    def getAdministator(self):
        """Gets the property: Administrator"""

        return self.__administartor