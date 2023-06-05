import unittest 
from unittest.mock import patch, call
from account import Account 

class TestFeature(unittest.TestCase):    
    @patch('builtins.print')
    def test_printStatement(self,mock_print):
        account = Account()
        account.deposit(1000) 
        account.deposit(2000)
        account.withdraw(500)
#-------------------------------- test_printStatement with multiple print statements -------------------
        account.printStatement()
        mock_print.assert_has_calls([
            call("DATE || AMOUNT || BALANCE"),
            call("14/01/2012 || -500 || 2500"),
            call("13/01/2012 || 2000 || 3000"),
            call("10/01/2012 || 1000 || 1000")
        ])
            
if __name__ == '__main__':
    unittest.main()