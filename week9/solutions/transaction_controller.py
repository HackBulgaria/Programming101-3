from models import Client, BankAccount


class TransactionController:
    
    def __init__(self, session):
        self.__session = session
    
    def create_account(self, user, account_name):
        account = BankAccount(balance=0, name=account_name)
        user.bank_accounts.append(account)

        self.__session.add(user)
        self.__session.commit()

        return account
