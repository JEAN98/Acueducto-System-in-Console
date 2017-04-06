import datetime
listReadsWaterMeters = []

class ReadsWaterMeter:

    def __init__(self,cubicMeters,waterMater,inspectorID):

        self.waterMeterID = waterMater.ID   #waterMeter is a object
        self.inpesctorID = inspectorID
        self.status = waterMater.status
        self.cubicMeters = cubicMeters
        now = datetime.datetime.now()
        plantillaFecha = "{}/{}/{}"
        self.fecha = plantillaFecha.format(now.day, now.month, now.year) #Get date time by sistem

        listReadsWaterMeters.append(self)   #Save the readsWater meters in listReadsWaterMeters

    def updateReadsWaterMeter(self,cubicMeters,waterMater,inspectorID,position):
        #Here can update reads

        self.waterMeterID = waterMater.ID  # waterMeter is a object
        self.inpesctorID = inspectorID
        self.status = waterMater.status
        self.cubicMeters = cubicMeters
        now = datetime.datetime.now()
        plantillaFecha = "{}/{}/{}"
        self.fecha = plantillaFecha.format(now.day, now.month, now.year)  # Get date time by sistem

        listReadsWaterMeters.pop(position) #Delete the old object

        listReadsWaterMeters.append(self) #Save the new object with Updates

    def searchReadWaterMeter(self,ID):
        for i in listReadsWaterMeters:
            if ID == i.waterMeterID:
                return i
        return False

    def deleteReadsWaterMeter(self,position):
        listReadsWaterMeters.pop(position) #Here can delete the information the object in listReadsWaterMeters
        del self       #Here can delete the object

    def getListReadsWater(self):
        return listReadsWaterMeters
