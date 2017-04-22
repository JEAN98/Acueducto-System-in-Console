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



       def updateStatus(self,ID):
            for i in waterMeterList:
                if ID == i.waterMeterID:
                  i.status = True  # Here can update the status , if the user pay for his water (False = Pending and True =  Pay Ready)
                  i.amountPrevious = i.amount # Amount previous, let us to find out how to person should pay for his or her water
                  print("Successful actualization!!")
                  return

