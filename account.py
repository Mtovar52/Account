from reto1 import AccountService
#IMPLENT INTERFACE AccountService
class Account(AccountService):
    def deposit(self, amount: int):
        raise NotImplementedError("error")
    def withdraw(self, amount: int):
        raise NotImplementedError("error")
    def printStatement(self):
        raise NotImplementedError("error")
