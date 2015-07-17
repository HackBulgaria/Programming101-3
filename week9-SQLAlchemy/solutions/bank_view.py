import sys


class BankView:

    def __init__(self, bank_controller):
        self.__bank = bank_controller
        self.__commands = {
            "user": {
                "create_account": self.create_account
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

    
    def __handle_login_error(self, message):
        print(message)

    def start_taking_commands(self):
        while True:
            if self.__user is None:
                self.__take_menu_command()
            else:
                self.__take_user_command()
            

    def login(self):
        username, password = self.__read_username_password()

        user = self.__bank.login(username, password)

        if not isinstance(user, str):
            self.__user = user
            print("You have logged in!")
            print("Hello {} with id {}".format(self.__user.username, self.__user.id))
        else:
            self.__handle_login_error(user)
    
    def register(self):
        username, password = self.__read_username_password()

        succ = self.__bank.register(username, password)

        if succ:
            print("You have registered successfuly. Login now")
        else:
            print("Username {} already taken".format(username))
    
    def create_account(self):
        account_name = input("Enter account name:")
        account = self.__bank.create_account(self.__user, account_name)
        
        print("Account with id {} was created".format(account.id))

    def help(self):
        pass

    def exit(self):
        sys.exit(0)
