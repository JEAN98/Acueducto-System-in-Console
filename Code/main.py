from Menu import *
from LogInSystem import *
from Colors import *
personID = ""

menu = Menu()
logIn = LogInSystem()
colors = Colors()

def menuApp():
    """Application main menu"""

    menu.menuPrincipal()

    option = input("Enter an option: ")

    print("")

    if option == "1":
        'Access system by ID and password'

        id = input("Enter your ID:\n")
        password = input("Enter you pasword:\n")

        log, admin = logIn.logIn(id, password)

        if log and admin:

            menu.menuAdministradores()

        elif log and not admin:

            menu.menuInspectores()

        else:

            print("\n{}Check the ID and password or Sign up{}\n".format(colors.getRed(),
                                                                        colors.getWhite()))

    elif option == "2":
        'Register system by ID and password'

        id = input("Enter your ID:\n")
        password = input("Enter you pasword:\n")
        admin = input("You are Administrator(y/n):\n")
        fullName = input("Enter your full name:\n")
        age = input("Enter your age:\n")
        email = input("Enter your email:\n")

        logIn.signUp(id, password, admin, fullName, age, email)

        print("{0}\nWelcome {2} to Aqueduct System Console{1}\n".format(colors.getGreen(),
                                                                        colors.getWhite(),
                                                                        fullName))

    elif option == "3":

        print("Good Bye")
        return

    else:

        print("{}The option is incorrect{}\n".format(colors.getRed(),
                                                     colors.getWhite()))

    menuApp()

menuApp()