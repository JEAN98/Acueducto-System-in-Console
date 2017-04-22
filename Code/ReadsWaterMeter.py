import  datetime
readsWaterMeterList = []
class ReadsWaterMeter:

    def __init__(self,cubicMeters,waterMater,inspectorID):

        self.waterMeterID = waterMater.ID   #waterMeter is a object
        self.inpesctorID = inspectorID
        self.status = False  #(False) = Pending and True =  Pay Ready
        self.cubicMeters = cubicMeters
        now = datetime.datetime.now()
        plantillaFecha = "{}/{}/{} {}:{}:{}"

        self.__fecha = plantillaFecha.format(now.day, now.month, now.year, now.hour, now.minute, now.second)
        readsWaterMeterList.append(self)
        print("Read water meter added!!")


    def updateReadsWaterMeter(self,ID,cubicMeters,period):
        #Here can update reads
        for i in readsWaterMeterList:
            if i.waterMeterID == ID:
                i.cubicMeters = cubicMeters
                i.period = period

                print("Successful actualization!!")
                return


    def printReadWaterMeter(self):
        #Here we can print a readWaterMeter

        print("***ReadWaterMeter ID: "+ str(self.waterMeterID)+"***"+"\n"+
              "InspectorID: "+str(self.inpesctorID) +"\n")
        if self.status == False:
            print("Status: Pending payment")
        else:
            print("Status: Ready payment")

        print("CubicMeters: "+str(self.cubicMeters))
        print("DateTime: "+str(self.period))

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

    def searchPendingInvoicesByClient(self, ownerID):
        # Maked a string that let us know the waterMeters pending for pay in our system
        resultPendigInvoices = "Pending invoices in these water meters: "

        # The cont variable let us know where we need to put the "," in our string
        cont = 0
        # The method search by ownerID, and then search all his watermeter that they need be payed
        for i in readsWaterMeterList:
            if i.ownerID == ownerID:
                if i.status == False:
                    if cont > 0:
                        resultPendigInvoices += " , "

                    resultPendigInvoices += str(i.waterMeterID)
                    cont += 1
        if cont > 0:
            return resultPendigInvoices
        else:
            return "No outstanding invoice!"

    def payWaterMer(self, waterMeterID):
        #In this method the admin can to make payments
        for i in readsWaterMeterList:
            if waterMeterID == i.waterMeterID:
                if i.status == False:
                    i.status = True
                    return "Payment ready, congratulations!!"
                else:
                    return "This water meter is already paid!"

