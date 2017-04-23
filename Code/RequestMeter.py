class RequestMeter:

    #el	ID	de	la	solicitud,	el	ID	del	abonado,	el	nombre	del	abonado,	la	dirección,	y	el	teléfono.
    def __init__(self, idRequest, idSubcriber, nameSubcriber, address, telephone):
        self.__idRequest = idRequest
        self.__idSubcriber = idSubcriber
        self.__nameSubscriber = nameSubcriber
        self.__address = address
        self.__telephone = telephone

    def getId(self):
        """Gets the property: ID"""

        return self.__idRequest

    def getIdSubcriber(self):
        """Gets the property: ID"""

        return self.__idSubcriber


    def getFullname(self):
        """Gets the property: Fullname"""

        return self.__nameSubscriber

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