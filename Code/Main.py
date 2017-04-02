from Menu import *

def menuApp():

    menu.menuPrincipal()

    option = int(input("Enter an option: "))

    print("")

    if option == 1:

        id = input("Enter your cedula:\n")
        password = input("Enter you pasword:\n")

    elif option == 2:
        pass

    elif option == 3:

        print("Good Bye")
        return

    else:

        print("The option is incorrect\n")

    menuApp()

menu = Menu()

menuApp()

