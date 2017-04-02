from Menu import *
from LogInSystem import *

def menuAdmin():
    print("admin")

def menuInspector():
    print("inspector")

def menuApp():
    'Application main menu'

    menu.menuPrincipal()

    option = int(input("Enter an option: "))

    print("")

    if option == 1:
        'Access system by ID and password'

        id = input("Enter your ID:\n")
        password = input("Enter you pasword:\n")

        log, admin = logIn.logIn(id, password)

        if  log and admin:

            menuAdmin()

        elif  log and admin != True:

            menuInspector()

        else:

            print("\nCheck the ID and password or Sign up\n")

    elif option == 2:
        'Register system by ID and password'

        id = input("Enter your ID:\n")
        password = input("Enter you pasword:\n")
        admin = input("You are Administrator(y/n):\n")
        fullName = input("Enter your full name:\n")
        age = input("Enter your age:\n")
        email = input("Enter your email:\n")

        logIn.signUp(id , password, admin, fullName, age, email)

        print("Welcome {} to Aqueduct System Console\n".format(fullName))

    elif option == 3:

        print("Good Bye")
        return

    else:

        print("The option is incorrect\n")

    menuApp()

menu = Menu()
logIn = LogInSystem()

menuApp()
