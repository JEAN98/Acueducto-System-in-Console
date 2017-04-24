from Subscriber import Subscriber

class Defaulter(Subscriber):

    def __init__(self, id, fullname, addres, telephone, meterId, debt):

        Subscriber.__init__(self, id, fullname, addres, telephone)

        self.__meterId = meterId
        self.__debt = debt

    def getDebt(self) -> object:
        return self.__debt

    def getMeterId(self):
        return self.__meterId

    def setDebt(self, debt: object) -> object:
        self.__debt = debt
