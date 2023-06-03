from reto1 import AccountService
#IMPLENT INTERFACE AccountService
class Account(AccountService):
    def deposit(self, amount: int):
        return amount
    def withdraw(self, amount: int):
        return amount
    def printStatement(self):
        pass
