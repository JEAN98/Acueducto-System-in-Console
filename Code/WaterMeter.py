# Class for waterMeter
listWaterMeters = []
class WaterMeter:

       def __init__(self, listRequest ,waterMeterID, amount):

           for i in listRequest:

               self.waterMeterID = waterMeterID
               self.OwnerID = i.ID
               self.status = False  # All water meters starts in False status    False = Pending and True =  Pay Ready
               self.amount = amount

               listWaterMeters.append(self)  #Save the objects on Global list


       def searchWaterMaterList(self,ID):
           for i in listWaterMeters:
               if ID == i.waterMeterID:
                   return i

           return False

       def getListWaterMeters(self):
           return listWaterMeters  #Return the list that have water meters objects


       def updateStatus(self,ID,position):
           for i in listWaterMeters:
               if ID == i.waterMeterID:
                   self.status = True  # Here can update the status , if the user pay for his water (False = Pending and True =  Pay Ready)
                   listWaterMeters[position].status = True #Update status in listWaterMeters
                   return True
           return False
