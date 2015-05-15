import sys


class BankView:

    def __init__(self, bank_controller):
        self.__bank = bank_controller
        self.__commands = {
            "user": {
            },
            "menu": {
                "register": self.register,
                "login": self.login,
            },
            "common": {
                "exit": self.exit,
                "help": self.help
            }
        }

        self.__user = None

    def __read_username_password(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        return (username, password)
    
    def __dispatch_command_from(self, command, command_state):
        states = [command_state, "common"]
        command_found = False

        for state in states:
            if command in self.__commands[state]:
                command_found = True
                self.__commands[state][command]()
                break

        if not command_found:
            print("Unknown command")

    def __take_menu_command(self):
        command = input("Enter command:" )
        self.__dispatch_command_from(command, "menu")


    def __take_user_command(self):
        command = input("What do you want to do? ")
        self.__dispatch_command_from(command, "user") 


    def start_taking_commands(self):
        while True:
            if self.__user is None:
                self.__take_menu_command()
            else:
                self.__take_user_command()
            

    def login(self):
        username, password = self.__read_username_password()

        try:
            self.__user = self.__bank.login(username, password)
            print("You have logged in!")
            print("Hello {} with id {}".format(self.__user.username, self.__user.id))
        except:
            print("Wrong username/password")
    
    def register(self):
        username, password = self.__read_username_password()

        succ = self.__bank.register(username, password)

        if succ:
            print("You have registered successfuly. Login now")
        else:
            print("Username {} already taken".format(username))
    
    def help(self):
        pass

    def exit(self):
        sys.exit(0)
