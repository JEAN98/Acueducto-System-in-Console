from RequestMeter import RequestMeter
from Colors import Colors

class RequestMeters:

    __listRequestMeters = []
    __idRequest = 3

    def __init__(self):
        self.__colors = Colors()
        self.__listRequestMeters.append(RequestMeter(1,
                                                     203200401,
                                                     "Enrique Segura Castro",
                                                     "100 meters West of San José De La Tigra school, San Carlos",
                                                     "24688071"))
        self.__listRequestMeters.append(RequestMeter(2,
                                                     200700134,
                                                     "Vanessa Rosales Ramos",
                                                     "150 meters North of San José De La Tigra school, San Carlos",
                                                     "24688329"))
        self.__listRequestMeters.append(RequestMeter(3,
                                                     201290710,
                                                     "Alexander Méndez Solera",
                                                     "200 meters Southeast of San José De La Tigra school, San Carlos",
                                                     "24688560"))

    def __str__(self):
        requestMeters = ""
        for request in self.__listRequestMeters:
            requestMeters += "{0}ID:{1} {2}" \
                             " {0}ID Subscriber:{1} {2}" \
                             " {0}Name:{1} {3}" \
                             " {0}Addres:{1} {4}" \
                             " {0}Telephone:{1} {5}\n".format(self.__colors.getBlue(),
                                                              self.__colors.getWhite(),
                                                              request.getId(),
                                                              request.getFullname(),
                                                              request.getAddres(),
                                                              request.getTelephone(),
                                                              request.getIdSubcriber())
        return requestMeters

    def addRequestMeter(self,idSubcriber, nameSubcriber, addres, telephone):
        self.__idRequest += 1
        requestMeters = RequestMeter(self.__idRequest, idSubcriber, nameSubcriber, addres, telephone)
        self.__listRequestMeters.append(requestMeters)