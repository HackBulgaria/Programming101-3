from bank_controller import BankController
from settings import DATABASE

controller = BankController(DATABASE)

while True:
    command = input("Enter command:")

    if command == "register":
        username = input("Enter username:")
        password = input("Enter password:")

        success = controller.register(username, password)


        if not success:
            print("Username already registered")
