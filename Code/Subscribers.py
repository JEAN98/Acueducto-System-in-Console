from Code.Colors import *
from Code.Subscriber import Subscriber

class Subscribers:

    __listSubscribers = []

    def __init__(self):

        self.__colors = Colors()

        self.__listSubscribers.append(Subscriber(2, "Juan Castellon", "Boca de Arenal", "77778888"))

        self.__listSubscribers.append(Subscriber(1, "Allan Castellon", "Boca de Arenal", "77778888"))

    def getList(self):
        'Return the list of subscribers'

        return self.__listSubscribers

    def addSubscribers(self,id , fullName, addres, telephone):
        """Add a user in the list subscribers.
        You need identification, full name, addres, telephone."""

        self.__listSubscribers.append(Subscriber(id, fullName, addres, telephone))

    def sortedList(self):
        'Sort the list subscribers'

        self.__listSubscribers = sorted(self.__listSubscribers, key= lambda subscriber: subscriber.getId() )

    def printList(self):

        for subscriber in self.__listSubscribers:
            print("{0}ID:{1} {2} {0}Name:{1} {3} {0}Addres:{1} {4} {0}Telephone:{1} {5}".format(self.__colors.getBlue(),
                                                                                                self.__colors.getWhite(),
                                                                                                subscriber.getId(),
                                                                                                subscriber.getFullname(),
                                                                                                subscriber.getAddres(),
                                                                                                subscriber.getTelephone()))