from Subscriber import Subscriber

class Defaulter(Subscriber):

    def __init__(self, id, fullname, addres, telephone,priceTotal,readingList):

        Subscriber.__init__(self, id, fullname, addres, telephone)

        self.__priceTotal = priceTotal
        self.__readingList = readingList

    def getreadingList(self):
        return self.__readingList

    def getpriceTotal(self):
        return self.__priceTotal

    def getNumReads(self):
        return len(self.__readingList)