import iban_algorithms

def get_input(text):
    return input(text)

def main():
    ibans_list_file_name = get_input("Input file name, which contains IBANS list: ")
    ibans_file_object = open(ibans_list_file_name, 'r')
    ibans = ibans_file_object.readlines() 
    ibans_file_object.close()
    valid_ibans_file = open("valid_ibans.txt", "a")
    invalid_ibans_file = open("invalid_ibans.txt", "a")
    for iban in ibans:
        iban = iban_algorithms.data_cleansing(iban)
        print("Checking " + iban + "...")
        if not (iban_algorithms.iban_check_digit(iban)):
            invalid_ibans_file.write(iban + " The IBAN is invalid. (Iban check digit)\n")
            print("The IBAN is invalid. (Iban check digit)\n")
            continue
        ####################################################################################
        #
        # TODO implement account number checking function, when it will be done in iban_algorithms.py file
        # if not (iban_algorithms.account_number_check(iban)):
        #   invalid_ibans_file.write(iban + " The IBAN is invalid. (Account number check)\n")
        #     print("The IBAN is invalid. (Account number check)\n")
        #     continue
        #
        ####################################################################################
        if not (iban_algorithms.iban_length(iban)): 
            invalid_ibans_file.write(iban + " The IBAN is invalid. (Length)\n")
            print("The IBAN is invalid. (Iban check digit)\n")
            continue
        ####################################################################################
        #
        # TODO implement format (structure) checking function, when it will be done in iban_algorithms.py file
        # if not (iban_algorithms.format_check(iban)):
        #   invalid_ibans_file.write(iban + " The IBAN is invalid. (Format (structure) check)\n")
        #     print("The IBAN is invalid. (Format (structure) check)\n")
        #     continue
        #
        ####################################################################################
        valid_ibans_file.write(iban + '\n')
        print("The IBAN is valid.\n")
    valid_ibans_file.close()
    invalid_ibans_file.close()

if __name__ == '__main__':
    main()