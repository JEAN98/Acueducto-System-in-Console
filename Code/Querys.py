from Defaulter import Defaulter
from Subscribers import Subscribers
from WaterMeter import *
from ReadsWaterMeter import *
from Colors import Colors

class Querys:

    __listDefaulters = []

    def __init__(self):
        self.__colors = Colors()
        self.__subscriber = Subscribers()

    def getListDefaulters(self, listReadings):

        for read in listReadings:
            for subriber in self.__subscriber.getList():
                if int(read.ownerID) == subriber.getId():
                    if not self.checkList(read.ownerID):
                        defaulter = Defaulter(read.ownerID,
                                              subriber.getFullname(),
                                              subriber.getAddres(),
                                              subriber. getTelephone(),
                                              self.calcAmount(read.ownerID),
                                              ReadsWaterMeter.getReadsByOwner(None,read.ownerID))
                        self.__listDefaulters.append(defaulter)

        self.__listDefaulters = sorted(self.__listDefaulters, key= lambda defaulter: defaulter.getNumReads() )
        self.__listDefaulters.reverse()

        i = 1
        defaulters = ""
        for defaulter in self.__listDefaulters:  #  id, fullname, addres, telephone,priceTotal
            defaulters += "{8}----------------------------------------------------------------------------------------------" \
                     "-------------------------------------------------------------------------------------------------{1}\n" \
                     "{7}) {0}Id Subscriber:{1} {2}" \
                     " {0}Name Subscriber:{1} {3}" \
                     " {0}Addres:{1} {4}" \
                     " {0}telephone:{1} {5}" \
                     " {0}Amount:{1} {6}\n".format(self.__colors.getBlue(),
                                                       self.__colors.getWhite(),
                                                       defaulter.getId(),
                                                       defaulter.getFullname(),
                                                       defaulter.getAddres(),
                                                       defaulter.getTelephone(),
                                                       defaulter.getpriceTotal(),
                                                       i,
                                                       self.__colors.getGreen())
            i += 1

            for read in defaulter.getreadingList():
                defaulters += "  - {0}Id Meter:{1} {2} " \
                         "{0}Meters Cubics:{1} {3} " \
                         "{0}Month:{1} {4} " \
                         "{0}State:{1} {5} " \
                         "{0}Id Inspector:{1} {6} " \
                         "{0}Amount:{1} {7}\n".format(self.__colors.getBlue(),
                                                      self.__colors.getWhite(),
                                                      read.waterMeterID,
                                                      read.cubicMeters,
                                                      read.period,
                                                      "canceled" if read.status else "pending payment",
                                                      read.inpesctorID,
                                                      read.price)
        return defaulters



    def checkList(self, idSubscriber):
        for defaulters in self.__listDefaulters:
            if defaulters.getId() == idSubscriber:
                return True
        return False

    def calcAmount(self, idSubscriber):
        amount = 0
        OwnerList = ReadsWaterMeter.getReadsByOwner(None, idSubscriber)
        for object in OwnerList:
            amount += object.price

        return amount


