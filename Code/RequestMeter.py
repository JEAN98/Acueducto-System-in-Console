class RequestMedidor:

    #el	ID	de	la	solicitud,	el	ID	del	abonado,	el	nombre	del	abonado,	la	dirección,	y	el	teléfono.
    def __init__(self, idRequest, idSubcriber, nameSubcriber, addres, telephone):
        self.__idRequest = idRequest
        self.__idSubcriber = idSubcriber
        self.__nameSubscriber = nameSubcriber
        self.__addres = addres
        self.__telephone = telephone