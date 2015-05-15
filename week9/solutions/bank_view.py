import sys


class BankView:

    def __init__(self, bank_controller):
        self.__bank = bank_controller
        self.__commands = {
            "register": self.register,
            "login": self.login,
            "exit": self.exit
        }

    def __read_username_password(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        return (username, password)

    def start_taking_commands(self):
        while True:
            command = input("Enter command: ")
            
            if command in self.__commands:
                self.__commands[command]()
            else:
                print("Unknown command")

    def login(self):
        username, password = self.__read_username_password()

        try:
            user = self.__bank.login(username, password)
            print("You have logged in!")
            print("Hello {} with id {}".format(user.username, user.id))
        except:
            print("Wrong username/password")
    
    def register(self):
        username, password = self.__read_username_password()

        succ = self.__bank.register(username, password)

        if succ:
            print("You have registered successfuly. Login now")
        else:
            print("Username {} already taken".format(username))

    def exit(self):
        sys.exit(0)
