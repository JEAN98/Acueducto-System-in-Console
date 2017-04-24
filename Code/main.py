from LogInSystem import LogInSystem
from Colors import Colors
from WaterMeter import WaterMeter
from Subscribers import Subscribers
from ReadsWaterMeter import *
import datetime
from RequestMeters import RequestMeters
from Querys import Querys

           #Owner,Code,amount
WaterMeter("2","222",0)
WaterMeter("1","111",100)
WaterMeter("205710037","1234",98)
                #Amount , Code, Inspector
ReadsWaterMeter(150,"222","2")
ReadsWaterMeter(250,"222","2")
ReadsWaterMeter(300,"111","2")
ReadsWaterMeter(60,"1234","2")


def __askInformationReadings(number):
    #Here we can ask the information any user and any times amount

    ID = input("Enter the water meter ID: ")
    reading = ReadsWaterMeter.searchReadWaterMeter(None, ID)

    if reading == 0:
        print("(xxxx)The ID wrote doesn't exist(xxxx)")
        print("")
        __askInformationReadings(number)
    else:
       if number =="2":
          cubicMeters = int(input("Enter the amount in cubic meter: "))
          ReadsWaterMeter.updateReadsWaterMeter(None,ID,cubicMeters)

       elif number=="3":
           ReadsWaterMeter.deleteReadsWaterMeter(reading)

    return

def __readsWaterMeterMenu():
    print("********Readings Menu ********\n",
                                "1) Print readings water meter\n",
                                "2) Update readings water meter \n",
                                "3) Delete readings water meter\n"
                                "4) Return")

    option = input("Select one option: ")

    if option == "1":
        ReadsWaterMeter.printAllReadWaterMeter(None) #Print all readings

    elif option == "2":
        __askInformationReadings("2")  #Called the method that let us ask about the information for Queries in readings

    elif option == "3":
        __askInformationReadings("3") #Called the method that let us ask about the information for Queries in readings

    elif option == "4":
        return

    __readsWaterMeterMenu()

def askInforAboutBilling(owner,ownerID,adminName,date):
    resultPending = ReadsWaterMeter.PendingInvoicesByClient(None,ownerID)  # Get the pending invoices by client, if don't have the method return null

    if resultPending != "null":
        print("Pending invoice in these waterMeter: " + resultPending)
        print("\n1)Cancel all invoices\n", "2)Cancel a specific invoice \n", "3)Return")

        option2 = input("Write the option: ")

        if option2 == "1":
            ReadsWaterMeter.PayWater(None, "")  # Pay all readings
            print("*****Bill*****")
            print("Owner ID: " + ownerID + "\nName: " + owner.getFullname() +
                  "\nPaid readings in these water meters: " + resultPending +
                  "\nAdmin name: " + adminName + "\nDate Time: " + date + "\n")

        elif option2 == "2":  # Pay one reading

            waterMeterID = input("Write the waterMeter ID: ")
            verificationWaterMeter = WaterMeter.searchWaterMeter(None,
                                                                 waterMeterID)  # Here we can verify if the watermeter wrote exist in system

            if verificationWaterMeter == "":
                print("The watermeterID wrote doesn't exist(xxxx)")
                __billingMenu()

            else:
                print("*****Bill*****")
                resultPayment = ReadsWaterMeter.PayWater(None,
                                                         waterMeterID)  # Get the pending invoices by client, if don't have the method return null
                if resultPayment:

                    print("Owner ID: " + ownerID + "\nName: " + owner.getFullname() +
                          "\nPaid reading in this water meter: " + resultPayment +
                          "\nAdmin name: " + adminName + "\nDate Time: " + date + "\n")
                else:
                    print("Payment had already been made")
        elif option2 == "3":
            return

        else:
            print("Character not defined!!")

    else:
        print("There are no pending readings!!")

def __billingMenu():

    #Here we can to make payments and review pending invoices
    adminName = __logIn.getUser().getFullName()  #Get the name of admin
    now = datetime.datetime.now()
    plantillaFecha = "{}/{}/{} {}:{}:{}"
    date = plantillaFecha.format(now.day, now.month, now.year, now.hour, now.minute, now.second)

    print("*******Billing Menu*******\n","1)Search pending invoice by Owner\n","2) Return\n")
    option = input("Enter a option: ")
    if option == "1":
        ownerID = input("Write the ownerID: ")
        owner = __subscribers.getSubscriber(ownerID) #Get the object of owner
        askInforAboutBilling(owner,ownerID,adminName,date)

    elif option == "2":

        return
    else:
        print("(xxxxx)Character incorrect\n")
        __billingMenu()

    __billingMenu()

def __menuAdministrators():

    print("{0}********ADMINISTRATOR MENU********{2}   ID: {3} User: {4}{1}\n".format(__colors.getBlue(),
                                                                                __colors.getWhite(),
                                                                                __colors.getOrange(),
                                                                                __logIn.getUser().getId(),
                                                                                __logIn.getUser().getFullName()),
          "1) Subscribers.\n",
          "2) Readings.\n",
          "3) Billing.\n",
          "4) Meter Requests.\n",
          "5) Queries.\n",
          "7) Logout.")

    option = input("Select one option: ")

    if option == "1":

        __menuSubscriber()

    elif option == "2":
        __readsWaterMeterMenu()

    elif option == "3":

        __billingMenu()


    elif option == "4":

        __menuRequestsMeters()


    elif option == "5":

        __menuQuerys()

    elif option == "7":

        print("Good Bye")
        return

    else:

        print("The option is incorrect\n")

    __menuAdministrators()

def __menuSubscriber():

    print("{0}********SUBSCRIBERS MENU ********{2}   ID: {3} User: {4}{1}\n".format(__colors.getBlue(),
                                                                                __colors.getWhite(),
                                                                                __colors.getOrange(),
                                                                                __logIn.getUser().getId(),
                                                                                __logIn.getUser().getFullName()),
          "1) Create Subscriber.\n",
          "2) Modify Subscriber.\n",
          "3) Delete Subscriber.\n",
          "4) View All Subscribers.\n",
          "5) View Subcribers by ID.\n",
          "6) Back.")
    option = input("Select one option: ")

    if option == "1":

        id = int(input("Enter the ID of subscriber:\n"))
        fullName = input("Enter the full name of subscriber:\n")
        addres = input("Enter the addres of subscriber:\n")
        telephone = input("Enter the telephone of subscriber:\n")

        __subscribers.addSubscribers(id, fullName, addres, telephone)
        __requestMeters.addRequestMeter(id, fullName, addres, telephone)

        print("{0}\nWas successfully added to{2}{1}\n".format(__colors.getGreen(),
                                                              __colors.getWhite(),
                                                              fullName))

    elif option == "2":

        oldId = int(input("Enter the old ID of subscriber:\n"))

        id = int(input("Enter the new ID of subscriber:\n"))
        fullName = input("Enter the full name of subscriber:\n")
        addres = input("Enter the addres of subscriber:\n")
        telephone = input("Enter the telephone of subscriber:\n")

        __subscribers.modifySubscribers(oldId, id, fullName, addres, telephone)

        print("{0}\nWas successfully modified to {2}{1}\n".format(__colors.getGreen(),
                                                              __colors.getWhite(),
                                                              fullName))

    elif option == "3":

        id = int(input("Enter the ID of subscriber:\n"))

        print("{0}\nWas successfully deleted to {2}{1}\n".format(__colors.getGreen(),
                                                                 __colors.getWhite(),
                                                                 __subscribers.deleteSubscribers(id)))

    elif option == "4":

        __subscribers.sortedList()
        __subscribers.printList()

    elif option == "5":

        id = int(input("Enter the ID of subscriber:\n"))

        __subscribers.printSubscriber(id)

    elif option == "6":

        return

    else:
        print("Invalid option")

    __menuSubscriber()

def __menuRequestsMeters():
    print("{0}********REQUESTS METERS MENU ********{2}   ID: {3} User: {4}{1}\n".format(__colors.getBlue(),
                                                                                    __colors.getWhite(),
                                                                                    __colors.getOrange(),
                                                                                    __logIn.getUser().getId(),
                                                                                    __logIn.getUser().getFullName()),
          "1) View All Requests Meters.\n",
          "2) View Request Meter by ID.\n",
          "3) View Request Meter by ID of the subscriber.\n",
          "4) Back.")

    option = input("Select one option: ")

    if option == "1":
        print(__requestMeters)

    elif option == "2":
        id = int(input("Enter the ID of requests:\n"))

        requests = __requestMeters.getRequestsMetersByID(id)

        print(requests)

    elif option == "3":
        id = int(input("Enter the ID of subscriber:\n"))

        requests = __requestMeters.getRequestsMetersByIDSubscribers(id)

        print(requests)

    elif option == "4":
        __menuAdministrators()
    else:
        pass

    __menuRequestsMeters()

def __menuQuerys():
    print("{0}********QUERYS MENU ********{2}   ID: {3} User: {4}{1}\n".format(__colors.getBlue(),
                                                                                    __colors.getWhite(),
                                                                                    __colors.getOrange(),
                                                                                    __logIn.getUser().getId(),
                                                                                    __logIn.getUser().getFullName()),
          "1) List of Defaulters.\n",
          "2) Modify Subscriber.\n",
          "3) Delete Subscriber.\n",
          "4) View All Subscribers.\n",
          "5) View Subcribers by ID.\n",
          "6) Back.")
    option = input("Select one option: ")

    if option == "1":
        print(__querys.getListDefaulters(readsWaterMeterList, waterMeterList))

def __menuInspectors():

    print("{0}********INSPECTOR MENU ********{2}   ID: {3} User: {4}{1}\n".format(__colors.getBlue(),
                                                                                __colors.getWhite(),
                                                                                __colors.getOrange(),
                                                                                __logIn.getUser().getId(),
                                                                                __logIn.getUser().getFullName()),
          "1)Water meter installaion.\n",
          "2)Make reads water meter.\n",
          "3)View All Requests Meters.\n",
          "4) Exit.")

    option = input("Select one option: ")

    if option == "1":
        #Water meter installaion
        # Serch if is in the list
        print("Write information for to install water meter!!")
        for i in __requestMeters.getRequestsMeters():
            print("Request: {}".format(__requestMeters.getRequestsMetersByID(i.getId())))
            waterMeterCode = input("Enter the water meter ID: ")
            amount = float(input("Enter the amount the water meter have: "))
            WaterMeter(i.getIdSubcriber(),waterMeterCode,amount)
            __requestMeters.deleteRequestMeter(i.getId())

        print("Succesful installation!")


    elif option == "2":
        #Make reads water meter

        waterMeterID = input("Enter the water meter ID: ")

        result = WaterMeter.searchWaterMeter(None,waterMeterID) #Search water Meter

        if result == "":
            print(waterMeterID+" Does not exist!!")
            __menuInspectors()
        else:
            cubicsMeter = float(input("Enter the get cubic meter: "))
            ReadsWaterMeter(cubicsMeter,waterMeterID,__logIn.getUser().getId())
            print("Reading water meter added!!")

    elif option == "3":
        print(__requestMeters)

    elif option == "4":

        return

    else:
        print("Invalid option")

    __menuInspectors()

def menuApp():
    """Application main menu"""

    print("{}*****Menu Principal*****{}".format(__colors.getBlue(), __colors.getWhite()))

    print("    1) Log In\n"
          "    2) Sign Up\n"
          "    3) Exit")

    option = input("Enter an option: ")

    print("")

    if option == "1":
        'Access system by ID and password'

        id = input("Enter your ID:\n")
        password = input("Enter you pasword:\n")

        __logIn.logIn(id, password)

        state = __logIn.getState()
        admin = __logIn.getUser().getAdministrator()

        if state and admin:

            __menuAdministrators()

        elif state and not admin:
            inspectorID = id
            __menuInspectors()

        else:

            print("\n{}Check the ID and password or Sign up{}\n".format(__colors.getRed(),
                                                                        __colors.getWhite()))

    elif option == "2":
        'Register system by ID and password'

        id = input("Enter your ID:\n")
        password = input("Enter you pasword:\n")
        admin = input("You are Administrator(y/n):\n")
        fullName = input("Enter your full name:\n")
        age = input("Enter your age:\n")
        email = input("Enter your email:\n")

        __logIn.signUp(id, password, admin, fullName, age, email)

        print("{0}\nWelcome {2} to Aqueduct System Console{1}\n".format(__colors.getGreen(),
                                                                        __colors.getWhite(),
                                                                        fullName))

    elif option == "3":

        print("Good Bye")
        return

    else:

        print("{}The option is incorrect{}\n".format(__colors.getRed(),
                                                     __colors.getWhite()))

    menuApp()

__logIn = LogInSystem()
__colors = Colors()
__subscribers = Subscribers()
__requestMeters = RequestMeters()
__querys = Querys()
menuApp()
