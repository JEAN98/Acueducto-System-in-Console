from Code.Colors import Colors
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


    def modifySubscribers(self, oldId, id , fullName, addres, telephone):
        """Modify a user in the list subscribers.
        You need old, identification, full name, addres, telephone."""

        i = 0
        while i < len(self.__listSubscribers):

            if oldId == self.__listSubscribers[i].getId():

                self.__listSubscribers[i].setId(id)
                self.__listSubscribers[i].setFullname(fullName)
                self.__listSubscribers[i].setAddres(addres)
                self.__listSubscribers[i].setTelephone(telephone)

            i += 1

    def deleteSubscribers(self, id):
        """Modify a user in the list subscribers.
        You need old, identification, full name, addres, telephone."""

        i = 0
        while i < len(self.__listSubscribers):

            if id == self.__listSubscribers[i].getId():

                copyName = self.__listSubscribers[i].getFullname()
                del self.__listSubscribers[i]
                return copyName

            i += 1


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
    def printSubscriber(self, id):

        for subscriber in self.__listSubscribers:

            if subscriber.getId() == id:

                print("{0}ID:{1} {2} {0}Name:{1} {3} {0}Addres:{1} {4} {0}Telephone:{1} {5}".format(self.__colors.getBlue(),
                                                                                                    self.__colors.getWhite(),
                                                                                                    subscriber.getId(),
                                                                                                    subscriber.getFullname(),
                                                                                                    subscriber.getAddres(),
                                                                                                    subscriber.getTelephone()))
