#
#   Data cleansing
#   This is used to remove all non-alphanumeric characters.
#
#   Returns string new_iban, which contains IBAN without non-alphanumeric characters.
#

def data_cleansing(iban):
    new_iban = ''
    for char in iban:
        if(char.isalnum()): new_iban += char
    return new_iban

#
#   Iban check digit
#   Integrity check on the IBAN using ISO 7064 (MOD 97-10) algorithm.
#

def iban_check_digit(iban):
    # Move the four initial characters to the end of the string (Rearrange).
    temp_iban = iban[4:] + iban[:4]
    # Replace the letters in the string with digits (Convert to integer).
    iban_converted_to_digits = ""
    for char in temp_iban:
        iban_converted_to_digits += str(ord(char)-55) if char.isalpha() else char
    # Convert the string to an integer and compute reminder.
    return(bool(int(iban_converted_to_digits)%97 == 1))

####################################################################################
#
#   TODO Account number check
#   Validation based on the country specific validation algorithms.
#
####################################################################################

#
#   Iban length
#   Verifying the total length of the IBAN according to the country standard.
#

#   Dictionary with country codes and their IBAN lengths.
#   This list is used for IBAN length checking.
iban_lengths = {
    "AL": 28,
    "AD": 24,
    "AT": 20,
    "AZ": 28,
    "BH": 22,
    "BY": 28,
    "BE": 16,
    "BA": 20,
    "BR": 29,
    "BG": 22,
    "CR": 22,
    "HR": 21,
    "CY": 28,
    "CZ": 24,
    "DK": 18,
    "DO": 28,
    "EG": 29,
    "SV": 28,
    "EE": 20,
    "FO": 18,
    "FI": 18,
    "FR": 27,
    "GE": 22,
    "DE": 22,
    "GI": 23,
    "GR": 27,
    "GL": 18,
    "GT": 28,
    "VA": 22,
    "HU": 28,
    "IS": 26,
    "IQ": 23,
    "IE": 22,
    "IL": 23,
    "IT": 27,
    "JO": 30,
    "KZ": 20,
    "XK": 20,
    "KW": 30,
    "LV": 21,
    "LB": 28,
    "LY": 25,
    "LI": 21,
    "LT": 20,
    "LU": 20,
    "MT": 31,
    "MR": 27,
    "MU": 30,
    "MD": 24,
    "MC": 27,
    "ME": 22,
    "NL": 18,
    "ML": 19,
    "NO": 15,
    "PK": 24,
    "PS": 29,
    "PL": 28,
    "PT": 25,
    "QA": 29,
    "RO": 24,
    "LC": 32,
    "SM": 27,
    "ST": 25,
    "SA": 24,
    "RS": 22,
    "SC": 31,
    "SK": 24,
    "SI": 19,
    "ES": 24,
    "SD": 18,
    "SE": 24,
    "CH": 21,
    "TL": 23,
    "TN": 24,
    "TR": 26,
    "UA": 29,
    "AE": 23,
    "GB": 22,
    "VG": 24
}

def iban_length(iban):
    country_code = iban[:2]
    # Check that the total IBAN length is correct as per the country.
    return(bool(iban_lengths[country_code] == len(iban)))

####################################################################################
#
# TODO Format (Structure)
# The IBAN's internal components are checked for correct format and respective positions.
#
####################################################################################