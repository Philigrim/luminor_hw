import unittest
import sys
sys.path.insert(1, '../Scripts')
import iban_algorithms

class TestIbanAlgorithms(unittest.TestCase):
    def test_data_cleansing(self):
        self.assertEqual(iban_algorithms.data_cleansing('GB82 WEST 1234 5698 7654 32'), 'GB82WEST12345698765432')
        
    def test_valid_iban_check_digit(self):
        self.assertTrue(iban_algorithms.iban_check_digit('GB82WEST12345698765432'))
    def test_invalid_iban_check_digit(self):
        self.assertFalse(iban_algorithms.iban_check_digit('GB8212345698765432WEST'))

    def test_valid_iban_length(self):
        self.assertTrue(iban_algorithms.iban_length('GB82WEST12345698765432'))
    def test_invalid_iban_length(self):
        self.assertFalse(iban_algorithms.iban_length('GB82WEST1234'))

if __name__ == "__main__":
    unittest.main()