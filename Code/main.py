"""Menu principal"""

from Worker import *

from Subscriber import *

def Test():

    worker1=Worker(000,"Jean",19,"Jean98vb@hotmail.com","asdfasdfa",1)

    if worker1.tipoTrabajador == 1:
        print("Tipo de trabajador: "+"Admin")
    else:
        print("Tipo de trabajador:"+ "User")

    print("Nombre: "+worker1.nombre)
    print("Email: "+worker1.email)



Test()










#Inspector main menu.

def inspectorMenu():
    print("********INSPECTOR MENU ********\n",
      "1) Install Meter.\n",
      "2) Realizar lectura.\n",
      "3) Exit.")


    option = input("Select one option: ")


    if option == "1":

        print("option#1")


    elif option == "2":

        print("option#2")


    elif option == "3":

        return


    else:
        print("Invalid option")







print ("X")


#Subscribers menu.

#def subscribersMenu():
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










#Administrator main menu.

#def administratorMenu():

    print("********ADMINISTRATOR MENU********\n",
      "1) Subscribers.\n",
      "2) Measuring.\n",
      "3) Billing.\n",
      "4) Meter Requests.\n",
      "5) Queries.\n",
      "6) Exit.")


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

        return


    else:
        print("Invalid option")










#Aqueduct main menu.

def mainMenu():

    print("********MENU********\n",
          "1) Log Ing.\n",
          "2) Sign Up.\n",
          "3) Exit.")


    option = input("Select one option: ")


    if option == "1":

        print("option#1")


    elif option == "2":

        print("option#2")


    elif option == "3":

        return


    else:
        print("Invalid option")


    menu()




menu()