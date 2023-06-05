from abc import ABC, abstractmethod
#----------------------------INTERFACE Reto1
class AccountService(ABC):
    @abstractmethod
    def deposit(self, amount: int):
        pass

    @abstractmethod   
    def withdraw(self,amount: int):
        pass
    
    @abstractmethod   
    def printStatement(self):
        pass
