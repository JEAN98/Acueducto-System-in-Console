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
        """Gets the property: Fullname"""

        return self.__fullname

    def getAddres(self):
        """Gets the property: Addres"""

        return self.__address

    def getTelephone(self):
        """Gets the property: Telephone"""

        return self.__telephone

    def setId(self, id):
        """Sets the property: ID"""

        self.__id = id

    def setFullname(self, fullname):
        """Sets the property: Fullname"""

        self.__fullname = fullname

    def setAddres(self, addres):
        """Sets the property: Addres"""

        self.__address = addres

    def setTelephone(self, telephone):
        """Sets the property: Telephone"""

        self.__telephone = telephone