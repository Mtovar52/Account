from reto1 import AccountService
import datetime
from transaction import TransactionDate
#--------------------------- AccountService "IMPLEMENTATION INTERFACE" ------------------------------
class Account(AccountService):
    
    def __init__(self):
        self.t = TransactionDate()
        self.listFeature = []
        self.balance = 0

    def deposit(self, amount: int):
        self.balance+=amount
        fecha = self.t.addDeposit()
        self.listFeature.append((fecha,amount,self.balance))
    
    def withdraw(self, amount: int):
        self.balance -= amount
        fecha = self.t.addwithdraw()
        self.listFeature.append((fecha,-amount,self.balance))
        
    def printStatement(self):
        print("DATE || AMOUNT || BALANCE")
        for feature in self.listFeature[::-1]:
            print(F"{feature[0]} || {feature[1]} || {feature[2]}")


        