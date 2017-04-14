from Code.Colors import Colors
from Code.WaterMeter import WaterMeter
from Code.Subscribers import Subscribers
from Code.ReadsWaterMeter import ReadsWaterMeter
requestList = [] #In this list we are going to save the request created by admin
 #in this list we are going to save the reads by inspectors
inspectorID=""
class Menu:

    def __init__(self):

        self.__colors = Colors()
        self.__subscribers  = Subscribers()

    def __menuPrincipal(self):
        'Print the main menu'

        print("{}*****Menu Principal*****{}".format(self.__colors.getBlue(), self.__colors.getWhite()))

        print("    1) Log In\n"
              "    2) Sign Up\n"
              "    3) Exit")

    def __menuAdministradores(self):

        print("{}********ADMINISTRATOR MENU********{}\n".format(self.__colors.getBlue(), self.__colors.getWhite()),
              "1) Subscribers.\n",
              "2) Measuring.\n",
              "3) Billing.\n",
              "4) Meter Requests.\n",
              "5) Queries.\n",
              "6) Logout.")

        option = input("Select one option: ")

        if option == "1":

            self.__menuSubscriber()

        elif option == "2":

            print("option#2")


        elif option == "3":

            print("option#3")


        elif option == "4":

            print("option#4")


        elif option == "5":

            print("option#5")

        elif option == "6":

            print("Good Bye")
            return

        else:

            print("The option is incorrect\n")

        self.getMenuAdministradores()

    def __menuSubscriber(self):

        print("{}********SUBSCRIBERS MENU ********{}\n".format(self.__colors.getBlue(), self.__colors.getWhite()),
              "1) Create Subscriber.\n",
              "2) Modify Subscriber.\n",
              "3) Delete Subscriber.\n",
              "4) View All Subscribers.\n",
              "5) View Subcribers by ID.\n",
              "6) Exit.")
        option = input("Select one option: ")

        if option == "1":

            id = int(input("Enter the ID of subscriber:\n"))
            fullName = input("Enter the full name of subscriber:\n")
            addres = input("Enter the addres of subscriber:\n")
            telephone = input("Enter the telephone of subscriber:\n")

            self.__subscribers.addSubscribers(id, fullName, addres, telephone)

            print("{0}\nWas successfully added to{2}{1}\n".format(self.__colors.getGreen(),
                                                               self.__colors.getWhite(),
                                                               fullName))

        elif option == "2":

            oldId = int(input("Enter the old ID of subscriber:\n"))

            id = int(input("Enter the new ID of subscriber:\n"))
            fullName = input("Enter the full name of subscriber:\n")
            addres = input("Enter the addres of subscriber:\n")
            telephone = input("Enter the telephone of subscriber:\n")

            self.__subscribers.modifySubscribers(oldId, id, fullName, addres, telephone)

            print("{0}\nWas successfully modified to {2}{1}\n".format(self.__colors.getGreen(),
                                                                  self.__colors.getWhite(),
                                                                  fullName))

        elif option == "3":

            id = int(input("Enter the ID of subscriber:\n"))

            print("{0}\nWas successfully deleted to {2}{1}\n".format(self.__colors.getGreen(),
                                                                     self.__colors.getWhite(),
                                                                     self.__subscribers.deleteSubscribers(id)))

        elif option == "4":

            self.__subscribers.sortedList()
            self.__subscribers.printList()

        elif option == "5":

            id = int(input("Enter the ID of subscriber:\n"))

            self.__subscribers.printSubscriber(id)

        elif option == "6":

            return

        else:
            print("Invalid option")

        self.getMenuSubscriber()

    def __menuInspectores(self):

        print("********INSPECTOR MENU ********\n",
              "1)Water meter installaion.\n",
              "2)Make reads water meter.\n",
              "3) Exit.")

        option = input("Select one option: ")

        if option == "1":
            #Water meter installaion
            # Serch if is in the list
            waterMeterCode = input("Enter the water meter ID: ")
            amount = float(input("Enter the amount the water meter have: "))
            newWaterMeter = WaterMeter(requestList,waterMeterCode,amount)




        elif option == "2":
            #Make reads water meter

            waterMeterID = input("Enter the water meter ID: ")
            waterMeterObj = WaterMeter.searchWaterMaterList(waterMeterID)

            if waterMeterObj == 0:
                print(waterMeterID+" Does not exist!!")
                Menu.menuInspectores(None)
            else:
                cubicsMeter = float(input("Enter the get cubic meter: "))
                ReadsWaterMeter(cubicsMeter,waterMeterObj,inspectorID)


        elif option == "3":

            return

        else:
            print("Invalid option")

        Menu.menuInspectores(None)

    def getMenuPrincipal(self):
        'Print the main menu'

        self.__menuPrincipal()

    def getMenuAdministradores(self):

        self.__menuAdministradores()

    def getMenuSubscriber(self):

        self.__menuSubscriber()

    def getMenuInspectors(self):

        self.__menuInspectores()
