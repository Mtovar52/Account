from collections import Counter

#----------------------- transaction date --------------------
class TransactionDate:

    def __init__(self):
        self.counter = -1
        self.listFechas = ["10/01/2012","13/01/2012","14/01/2012"]

    def addDeposit(self):
        self.counter += 1
        return self.listFechas[self.counter]
        
    def addwithdraw(self):
        self.counter += 1
        return self.listFechas[self.counter]