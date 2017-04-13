class Subscriber:

    def __init__(self, id, fullname, addres, telephone):

        self.__id = id
        self.__fullname = fullname
        self.__address = addres
        self.__telephone = telephone

    def getId(self):
        """Gets the property: ID"""

        return self.__id


    def getFullname(self):
        """Gets the property: ID"""

        return self.__fullname

    def getAddres(self):
        """Gets the property: ID"""

        return self.__address

    def getTelephone(self):
        """Gets the property: ID"""

        return self.__telephone