import unittest 
from unittest.mock import MagicMock, patch
from account import Account 

class TestFeature(unittest.TestCase):    
    
    @patch('builtins.print')
    def test_printStatement(self,mock):
        
        Account.deposit(self, 4000)
        Account.withdraw(self, 400)
        Account.deposit(self, 1000)

        mock = MagicMock()
        with patch('time.strftime', return_value='14/01/2012'):
            Account.printStatement(self)
            mock.assert_called_with("14/01/2012 || 1000   || 4600")

        with patch('time.strftime', return_value='13/01/2012'):
            Account.printStatement(self)
            mock.assert_called_with("13/01/2012 || -400   || 3600")

        with patch('time.strftime', return_value='10/01/2012'):
            Account.printStatement(self)
            mock.assert_called_with("10/01/2012 || 4000   || 4000")

if __name__ == '__main__':
    unittest.main()