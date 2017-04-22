# Class for waterMeter
waterMeterList=[]
class WaterMeter:

       def __init__(self, OwnerID ,waterMeterID, amount):

           self.waterMeterID = waterMeterID
           self.OwnerID = OwnerID #Get in requestList
           self.amount = amount
           waterMeterList.append(self)

       def updateCubicMeters(self, ID,newAmount):
           #Here we can Update the cubicMeters
          for i in waterMeterList:
               if ID == i.waterMeterID:
                    i.amount = newAmount


       def searchWaterMeter(self,waterMeterID):
           for i in waterMeterList:
               if waterMeterID == i.waterMeterID:
                   return waterMeterID
           return ""

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



