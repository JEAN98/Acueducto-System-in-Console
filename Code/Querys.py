from Defaulter import Defaulter
from Subscribers import Subscribers
from Colors import Colors

class Querys:

    __listDefaulters = []

    def __init__(self):
        self.__colors = Colors()

    def getListDefaulters(self, listReadings, listMeters):
        listPending = []
        for reading in listReadings:
            if not reading.status:
                listPending.append(reading)

        subscribers = Subscribers()
        for meters in listMeters:

            for pending in listPending:
                if meters.waterMeterID == pending.waterMeterID:
                    subscriber = subscribers.getSubscriber(meters.OwnerID)
                    self.__listDefaulters.append(Defaulter( subscriber.getId(),
                                                            subscriber.getFullname(),
                                                            subscriber.getAddres(),
                                                            subscriber.getTelephone(),
                                                            meters.waterMeterID,
                                                            pending.calculateInvoice(meters.waterMeterID, 0)))

        listDefaulters = []

        for defaulter in self.__listDefaulters:
            if listDefaulters != []:
                for defau in listDefaulters:
                    if defaulter.getId() == defau.getId():
                        tmp = defau.getDebt()
                        tmp += defaulter.getDebt()

                        defau.setDebt(tmp)
                    else:
                        listDefaulters.append(defaulter)
            else:
                listDefaulters.append(defaulter)

        self.__listDefaulters = listDefaulters

        self.__listDefaulters = sorted(self.__listDefaulters, key=lambda defaulter: defaulter.getDebt())
        self.__listDefaulters.reverse()

        defaulters = ""
        i = 1

        for defaulter in self.__listDefaulters:
            defaulters += "{9}{8}){1} " \
                          "{0}ID:{1} {2} " \
                          "{0}Name:{1} {3} " \
                          "{0}Addres:{1} {4} " \
                          "{0}Telephone:{1} {5} " \
                          "{0}Meter ID:{1} {6} " \
                          "{0}Debt:{1} {7}\n".format(self.__colors.getBlue(),
                                                     self.__colors.getWhite(),
                                                     defaulter.getId(),
                                                     defaulter.getFullname(),
                                                     defaulter.getAddres(),
                                                     defaulter.getTelephone(),
                                                     defaulter.getMeterId(),
                                                     defaulter.getDebt(),
                                                     i,
                                                     self.__colors.getGreen())
            i += 1

        return defaulters