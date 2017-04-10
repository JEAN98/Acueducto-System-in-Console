from Code.Colors import Colors
from WaterMeter import *
from ReadsWaterMeter import *
requestList = [] #In this list we are going to save the request created by admin
 #in this list we are going to save the reads by inspectors
inspectorID=""
class Menu:

    def __init__(self):

        self.__colors = Colors()

    def menuPrincipal(self):
        'Print the main menu'

        print("{}*****Menu Principal*****{}".format(self.__colors.getBlue(), self.__colors.getWhite()))

        print("    1) Log In\n"
              "    2) Sign Up\n"
              "    3) Exit")

    def menuAdministradores(self):

        print("{}********ADMINISTRATOR MENU********{}\n".format(self.__colors.getBlue(), self.__colors.getWhite()),
              "1) Subscribers.\n",
              "2) Measuring.\n",
              "3) Billing.\n",
              "4) Meter Requests.\n",
              "5) Queries.\n",
              "6) Logout.")

        option = input("Select one option: ")

        if option == "1":

            print("option#1")


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

    def menuAbonados(self):

        print("********SUBSCRIBERS MENU ********\n",
              "1) Create Subscriber.\n",
              "2) Modify Subscriber.\n",
              "3) Delete Subscriber.\n",
              "4) Exit.")
        option = input("Select one option: ")

        if option == "1":

            print("option#1")


        elif option == "2":

            print("option#2")


        elif option == "3":

            print("option#3")


        elif option == "4":

            return


        else:
            print("Invalid option")

    def menuInspectores(self):

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
                print(waterMeterID+" Does´not exist!!")
                Menu.menuInspectores(None)
            else:
                cubicsMeter = float(input("Enter the get cubic meter: "))
                ReadsWaterMeter(cubicsMeter,waterMeterObj,inspectorID)


        elif option == "3":

            return

        else:
            print("Invalid option")

        Menu.menuInspectores(None)