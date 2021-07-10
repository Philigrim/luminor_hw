import iban_algorithms
import sys

def get_input(text):
    return input(text)

def main():
    iban = iban_algorithms.data_cleansing(get_input("Input IBAN, that you want to check: "))
    if not (iban_algorithms.iban_check_digit(iban)): sys.exit("The IBAN is invalid. (Iban check digit)")
    ####################################################################################
    #
    #   TODO Implement account number checking function, when it will be done in iban_algorithms.py file
    #   Validation based on the country specific validation algorithms.
    #
    #   if not (iban_algorithms.account_number_check(iban)): sys.exit("The IBAN is invalid. (Based on the country specific validation)")
    #
    ####################################################################################
    if not (iban_algorithms.iban_length(iban)): sys.exit("The IBAN is invalid. (Length)")
    ####################################################################################
    #
    # TODO Implement format (structure) checking function, when it will be done in iban_algorithms.py file
    # The IBAN's internal components are checked for correct format and respective positions.
    #
    # if not (iban_algorithms.format_check(iban)): sys.exit("The IBAN is invalid. (Based on the country specific validation)")
    #
    ####################################################################################
    print(iban + " is valid.")


if __name__ == '__main__':
    main()