import  datetime
from WaterMeter import *

readsWaterMeterList = []
waterPayConsume =[]

class ReadsWaterMeter:

    def __init__(self,cubicMeters,waterMeterID,inspectorID):

        self.waterMeterID = waterMeterID  #waterMeter is a object
        self.inpesctorID = inspectorID
        self.status = False  #(False) = Pending and True =  Pay Ready
        self.cubicMeters = cubicMeters
        now = datetime.datetime.now()
        plantillaFecha = "{}/{}/{} {}:{}:{}"

        self.period = plantillaFecha.format(now.day, now.month, now.year, now.hour, now.minute, now.second)
        self.lastModified = plantillaFecha.format(now.day, now.month, now.year, now.hour, now.minute, now.second)
        self.price = 0
        readsWaterMeterList.append(self)


        ReadsWaterMeter.calculatePrice(self)
        WaterMeter.updateCubicMeters(None,waterMeterID,cubicMeters)

    def getReadsWaterMeter(self):
        return readsWaterMeterList

    def updateReadsWaterMeter(self,ID,cubicMeters):
        #Here can update reads
        now = datetime.datetime.now()
        plantillaFecha = "{}/{}/{} {}:{}:{}"
        for i in readsWaterMeterList:
            if i.waterMeterID == ID:
                i.cubicMeters = cubicMeters
                i.lastModified = plantillaFecha.format(now.day, now.month, now.year, now.hour, now.minute, now.second)

                print("Successful actualization!!")
                print("")
                return


    def printReadWaterMeter(self):
        #Here we can print a readWaterMeter

        print("\n***Reading in ID: "+ str(self.waterMeterID)+"***"+"\n"+
              "InspectorID: "+self.inpesctorID)
        if self.status == False:
            print("Status: Pending payment")
        else:
            print("Status: Ready payment")

        print("CubicMeters: "+str(self.cubicMeters))
        print("DateTime: "+ self.period)
        print("Last modified: "+self.lastModified)
        print("*************************\n")

    def printAllReadWaterMeter(self):
        #Here we can print all readsWaterMeter

        for reading in readsWaterMeterList:
            ReadsWaterMeter.printReadWaterMeter(reading)   #Call method in same class that can to print little by little


    def printReadingWaterMeter(self,waterMeterID):
        # Here we can print a readingWaterMeter

        for reading in readsWaterMeterList:
            if reading.waterMeterID == waterMeterID:
                ReadsWaterMeter.printReadWaterMeter(reading) # Call method in same class that can to print


    def searchReadWaterMeter(self, waterMeterID):
        #In this method can search a reading of any water meter

       for i in readsWaterMeterList:
           if waterMeterID == i.waterMeterID:
                return i
       return 0   #If this method can to return 0 is because does not exist



    def deleteReadsWaterMeter(self):
        # Here can delete the information the reading in listReadsWaterMeters
        readsWaterMeterList.remove(self)
        print("Successful elimination!!")
        print("")



    def PayWater(self,waterMeterID):
        #In this method the admin can to make payments
        price=0
        for i in readsWaterMeterList:
            if waterMeterID == "": #If USER is going to pay all
                if i.status == False:

                    i.status = True #Payment ready
                    WaterMeter.updateCubicMeters(None, i.waterMeterID, i.cubicMeters)
                    waterPayConsume.append(i)


            elif waterMeterID == i.waterMeterID: #If USER is going to pay one reading

                if i.status == False:

                    i.status = True #Payment ready
                    WaterMeter.updateCubicMeters(None, i.waterMeterID, i.cubicMeters)
                    waterPayConsume.append(i)
                    price += i.price

        return "Total price: " + str(i.price)





    def calculatePrice(self):

        for reading in readsWaterMeterList:
            if reading == self:
                oldAmount = WaterMeter.getRecentCubicMeters(None,reading.waterMeterID) #we need search the old amount,


                if reading.cubicMeters - oldAmount > 80:

                    price = (((reading.cubicMeters - oldAmount) - 80)*0.1)+4  #Determination of price
                    reading.price = price
                    return

                else:

                    reading.price = 4
                    return




    def PendingInvoicesByClient(self,ownerID):

        waterMeterListbyOwner = WaterMeter.getWaterMetersByOwner(None,ownerID)
        # Make a string that let us know the waterMeters pending for pay in our system
        resultPendigInvoices = " "
        totalPrice = 0
        # The cont variable let us know where we need to put the "," in our string
        cont = 0
        # The method search by ownerID, and then search all his watermeter that they need be payed
        for i in waterMeterListbyOwner:
            for j in readsWaterMeterList:

                if j.waterMeterID == i.waterMeterID and j.status == False:
                    if cont > 0:
                        resultPendigInvoices += " , "  # Add character

                    resultPendigInvoices += "ID " + str(j.waterMeterID) + " $"+str(j.price)
                    totalPrice += j.price #Accumulated from all debts
                    cont += 1

        if cont > 0:
            return resultPendigInvoices + "\nTotal price: $" + str(totalPrice)

        else:
            return "null"



    def getListConsumeWater(self):
        return waterPayConsume