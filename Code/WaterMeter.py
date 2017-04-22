# Class for waterMeter
waterMeterList=[]
class WaterMeter:

       def __init__(self, requestList ,waterMeterID, amount):

           for i in requestList:

               self.waterMeterID = waterMeterID
               self.OwnerID = i.OwnerID #Get in requestList
               self.amount = amount
               waterMeterList.append(self)

       def updateCubicMeters(self, ID,newAmount):
           #Here we can Update the cubicMeters
          for i in waterMeterList:
               if ID == i.waterMeterID:
                    i.amount = newAmount

       def getCubicMeters(self,ID):
            for i in waterMeterList:
                if ID == i.waterMeterID:
                    return i.amount

       def getWaterMetersByOwner(self,ownerID):
           waterMeterByOwnerList =[]
           for waterMeter in waterMeterList:
               if waterMeter.OwnerID == ownerID:
                   waterMeterByOwnerList.append(waterMeter)

           return waterMeterByOwnerList


