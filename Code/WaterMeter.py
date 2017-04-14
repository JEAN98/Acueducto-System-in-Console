# Class for waterMeter
waterMeterList=[]
class WaterMeter:

       def __init__(self, requestList ,waterMeterID, amount):

           for i in requestList:

               self.waterMeterID = waterMeterID
               self.OwnerID = i.OwnerID #Get in requestList
               self.status = False  # All water meters starts in False status    False = Pending and True =  Pay Ready
               self.amount = amount
               self.amountPrevious = amount
               waterMeterList.append(self)

       def printWaterMeter(self):
           #Here we can to print object that exist in list

           print("***Water meter: "+ str(self.waterMeterID)+"***")
           print("OwnerID: "+str(self.OwnerID))
           if self.status == False:
               print("Status: Pending payment")
           else:
               print("Status: Ready payment")

           print("Amount in the waterMeter: "+str(self.amount))



       def searchWaterMaterList(self, ID):
          for i in waterMeterList:
               if ID == i.waterMeterID:
                 return i

          return 0  ##If this method can to return 0 is because does not exist

       def updateStatus(self,ID,newAmount):
            for i in waterMeterList:
                if ID == i.waterMeterID:
                  i.status = True  # Here can update the status , if the user pay for his water (False = Pending and True =  Pay Ready)
                  i.amountPrevious = i.amount # Amount previous, let us to find out how to person should pay for his or her water
                  print("Successful actualization!!")
                  return


