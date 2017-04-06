from Colors import *

class Subscribers:

    __listSubscribers = []

    def __init__(self):

        self.__colors = Colors()

        self.__listSubscribers.append({"id": "2",
                                       "fullName": "Juan Castellon",
                                       "addres": "Boca de Arenal",
                                       "telephone": "77778888"})

        self.__listSubscribers.append({"id": "1",
                                 "fullName": "Allan Castellon",
                                 "addres": "Boca de Arenal",
                                 "telephone": "77778888"})

    def getList(self):
        'Return the list of subscribers'

        return self.__listSubscribers

    def addSubscribers(self,id , fullName, addres, telephone):
        """Add a user in the list subscribers.
        You need identification, full name, addres, telephone."""

        self.__listSubscribers.append({"id": id,
                                 "fullName": fullName,
                                 "addres": addres,
                                 "telephone": telephone})

    def sortedList(self):
        'Sort the list subscribers'

        self.__listSubscribers = sorted(self.__listSubscribers, key= lambda subscribers: subscribers["id"] )

    def printList(self):

        for subscriber in self.__listSubscribers:
            print("{0}ID:{1} {2} {0}Name:{1} {3} {0}Addres:{1} {4} {0}Telephone:{1} {5}".format(self.__colors.blue(),
                                                                                                self.__colors.white(),
                                                                                                subscriber["id"],
                                                                                                subscriber["fullName"],
                                                                                                subscriber["addres"],
                                                                                                subscriber["telephone"]))