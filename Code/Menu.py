class Menu:

    def menuPrincipal(self):
        'Print the main menu'

        print("*****Menu Principal*****")

        print("    1) Log In\n"
              "    2) Sign Up\n"
              "    3) Exit")

    def menuAdministradores(self):

        print("********ADMINISTRATOR MENU********\n",
              "1) Subscribers.\n",
              "2) Measuring.\n",
              "3) Billing.\n",
              "4) Meter Requests.\n",
              "5) Queries.\n",
              "6) Logout.")

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