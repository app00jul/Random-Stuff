##########################################
# Name: Julian Noeske
##########################################
from math import floor  # E.g., floor(5.3) -> 5, floor(3.9) -> 3
from functools import reduce
import string

######################################################################
# Task 1: Given an 8-digit decimal number representing the date,
#         calculate the day of the week using Zeller's congruence:
#
#           https://en.wikipedia.org/wiki/Zeller%27s_congruence
#
# Input:  8-digit decimal number in the format of YYYYMMDD
#
# Output: Weekday as a [0-6] number, where
#         0: Saturday, 1: Sunday, 2: Monday, ..., 6: Friday
######################################################################

def getWeekday(date):
    year = int(date) // 10000
    month_day = int(date) % 10000
    month = month_day // 100
    day = month_day % 100

    """print(f"\nThe year is \t {year}")
    print(f"The month is \t {month}")
    print(f"The day is \t \t {day}")""" #this is for debugging


    if month == 1 or month == 2:
        m = month + 12
        year = year -1
        #print(m) #this is for debugging!
    else:
        m = month
        year = year
        #print(m) #this is for debugging!
    J = year//100
    K = year%100
    h = (day + (13*(m + 1))//5 + K + K//4 + J//4 - 2*J)%7
    #print(h) #this is for debugging!
    if h == 0:
        return ("The day is Saturday!")
    elif h == 1:
        return ("The day is Sunday!")
    elif h == 2:
        return ("The day is Monday!")
    elif h == 3:
        return ("The day is Tuesday!")
    elif h == 4:
        return ("The day is Wednesday!")
    elif h == 5:
        return ("The day is Thursday!")
    elif h == 6:
        return ("The day is Friday!")

print(getWeekday(20000101))


##############################date########################################
# Task 2: Create two functions, an encoder and a decoder for the
#         Caesar cipher:
#
#           https://en.wikipedia.org/wiki/Caesar_cipher
#
# Note: You can try out this cipher at the link below:
#
#           https://cryptii.com/pipes/caesar-cipher
######################################################################

######################################################################
# This provided helper function may be useful
# Input:  List of ASCII values (Ex: [72, 69, 76, 76, 79])
# Output: String (Ex. 'HELLO')       'H   E   L   L   O'd helper function may be useful
# Input:  List of ASCII values (Ex: [72, 69, 76, 76, 79])
# Output: String (Ex. 'HELLO')       'H   E   L   L   O'
######################################################################
def asciiToString(asciiList):
    return ''.join(map(chr, asciiList))

######################################################################
# Caesar Encoder
#
# Input: A string (assume all-caps: leave everything else as-is),
#        and a shift value       (Ex. 'HELLO WORLD', 3)
#
# Output: An encoded string      (Ex. 'KHOOR ZRUOG')
#
# Hint: The ord() function converts single-character strings to ASCII
#       (Its inverse, the chr() function, is used in the provided helper)
######################################################################

def caesarEncoder(str, shift):
    lst_convert = list(str)
    #print(lst_convert) #this is for debugging

    ascii_convert = map(lambda x: ord(x), lst_convert)
    #print(ascii_convert) #this is for debugging

    caesar_encoder = map(lambda x: x + shift if x != 32 else 32, ascii_convert)

    caesar_encoder_final = map(lambda x: x - 26 if x > 90 else x, caesar_encoder)
    return asciiToString(caesar_encoder_final)

print(caesarEncoder("MORETESTING", 26))

######################################################################
# Decoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. KHOOR ZRUOG, 3)
# Output: A decoded string             (Ex. HELLO WORLD)
# Hint: The chr() function converts ASCII to a single-character string
######################################################################
def caesarDecoder(str, shift):
    lst_convert = list(str)
    # print(lst_convert) #this is for debugging

    ascii_convert = map(lambda x: ord(x), lst_convert)
    # print(ascii_convert) #this is for debugging

    caesar_decoder = map(lambda x: x - shift if x != 32 else 32, ascii_convert)
    caesar_decoder_final = map(lambda x: x + 26 if x <65 else x, caesar_decoder)
    return asciiToString(caesar_decoder_final)


print(caesarDecoder("MORETESTING",26))  
