import unittest
from unittest.mock import patch
import sys
sys.path.insert(1, '../Scripts')
import iban_list_check
from io import StringIO
import os

class TestIbanList(unittest.TestCase):
    @patch('iban_list_check.get_input', return_value='ibans_for_testing.txt')
    def test_iban_list_check_printed_output(self, input):
        out = StringIO()
        sys.stdout = out
        iban_list_check.main()
        output = "Checking GB33BUKB20201555555555...\nThe IBAN is valid.\n\n"
        output += "Checking DE75512108001245126199...\nThe IBAN is valid.\n\n"
        output += "Checking FR7630006000011234567890189...\nThe IBAN is valid.\n\n"
        output += "Checking GB82WEST123456...\nThe IBAN is invalid. (Iban check digit)\n\n"
        output += "Checking GB82WEST12345698765432...\nThe IBAN is valid.\n\n"
        self.assertEqual(out.getvalue(), output)
        os.remove('invalid_ibans.txt')
        os.remove('valid_ibans.txt')

if __name__ == "__main__":
    unittest.main()
    # GB82 WEST 1234 5698 7654 3