import unittest
from unittest.mock import patch
import sys
sys.path.insert(1, '../Scripts')
import single_iban_check
from io import StringIO

class TestSingleIban(unittest.TestCase):
    @patch('single_iban_check.get_input', return_value='GB82WEST12345698765432')
    def test_valid_single_iban_check(self, input):
        out = StringIO()
        sys.stdout = out
        single_iban_check.main()
        self.assertEqual(out.getvalue(), "GB82WEST12345698765432 is valid.\n")

if __name__ == "__main__":
    unittest.main()