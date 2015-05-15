from bank_controller import BankController
from bank_view import BankView
from settings import DATABASE

controller = BankController(DATABASE)
view = BankView(controller)

view.start_taking_commands()

