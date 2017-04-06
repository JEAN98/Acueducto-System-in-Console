from Code.Menu import Menu
from Code.LogInSystem import LogInSystem
from Code.Colors import Colors
personID = ""


class Main:

    def menuApp(self):
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

                print("\n{}Check the ID and password or Sign up{}\n".format(colors.red(),
                                                                            colors.white()))

        elif option == "2":
            'Register system by ID and password'

            id = input("Enter your ID:\n")
            password = input("Enter you pasword:\n")
            admin = input("You are Administrator(y/n):\n")
            fullName = input("Enter your full name:\n")
            age = input("Enter your age:\n")
            email = input("Enter your email:\n")

            logIn.signUp(id, password, admin, fullName, age, email)

            print("{0}\nWelcome {2} to Aqueduct System Console{1}\n".format(colors.green(),
                                                                            colors.white(),
                                                                            fullName))

        elif option == "3":

            print("Good Bye")
            return

        else:

            print("{}The option is incorrect{}\n".format(colors.red(),
                                                         colors.white()))

        self.menuApp()

main = Main()
menu = Menu()
logIn = LogInSystem()
colors = Colors()

main.menuApp()
