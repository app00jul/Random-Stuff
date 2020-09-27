# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

num = int(input("Please enter a random number: "))

if num > 1:
    for i in range(2, num):
        if (num%i) == 0:
            print(num, " is not a prime number!")
            break
        else:
            print(num, " is a prime number!!!!!")

else:
    print(num, " is not a prime number!")
