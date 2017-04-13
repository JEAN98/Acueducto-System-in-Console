import datetime
readsWaterMeterList = []
class ReadsWaterMeter:

    def __init__(self,cubicMeters,waterMater,inspectorID):

        self.waterMeterID = waterMater.ID   #waterMeter is a object
        self.inpesctorID = inspectorID
        self.status = waterMater.status
        self.cubicMeters = cubicMeters
        now = datetime.datetime.now()
        plantillaFecha = "{}/{}/{}"
        self.fecha = plantillaFecha.format(now.day, now.month, now.year) #Get date time by sistem
        readsWaterMeterList.append(self)
        print("Read water meter added!!")


    def updateReadsWaterMeter(self,cubicMeters,waterMater,inspectorID):
        #Here can update reads
        for i in readsWaterMeterList:
            if i == self:

                i.waterMeterID = waterMater.ID  # waterMeter is a object
                i.inpesctorID = inspectorID
                i.status = waterMater.status
                i.cubicMeters = cubicMeters
                now = datetime.datetime.now()
                plantillaFecha = "{}/{}/{}"
                i.fecha = plantillaFecha.format(now.day, now.month, now.year)  # Get date time by sistem
                print("Successful actualization!!")


    def printReadWaterMeter(self):
        #Here we can print a readWaterMeter

        print("***ReadWaterMeter ID: "+ str(self.waterMeterID)+"***"+"\n"+
              "InspectorID: "+str(self.inpesctorID) +"\n")
        if self.status == False:
            print("Status: Pending payment")
        else:
            print("Status: Ready payment")

        print("CubicMeters: "+str(self.cubicMeters))
        print("DateTime: "+str(self.fecha))

    def printAllReadWaterMeter(self):
        #Here we can print all readsWaterMeter
        for read in readsWaterMeterList:
            ReadsWaterMeter.printReadWaterMeter(read)   #Call method in same class that can to print little by little

    def searchReadWaterMeter(self,ID):
       for i in readsWaterMeterList:
           if ID == i.waterMeterID:
                return i
       return 0   #If this method can to return 0 is because does not exist


    def deleteReadsWaterMeter(self):
        readsWaterMeterList.remove(self) #Here can delete the information the object in listReadsWaterMeters
        print("Successful elimination!!")

