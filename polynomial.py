############################################################
# CS115 Lab 4
# Name: Julian Noeske
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
############################################################

from functools import reduce

# Task 1: Use reduce to add up all elements in a list
"""
Input: A list of numbers
Output A number representing the sum
Example: add_all([1, 2, 3]) = 6
"""
def add_all(lst):
    sum = reduce(lambda x,y: x+y, lst)
    print(sum)
    return sum

lst_1 = [1,4,6]
add_all(lst_1)

# Task 2: Use map to evaluate a given polynomial at a specific x-value
"""
Input:
  p: A list of coefficients for increasing powers of x
  x: The value of x to evaluate
Output: Number representing the value of the evaluated polynomial
Example: poly_eval([1, 2, 3], 2) = 1(2)^0 + 2(2)^1 + 3(2)^2 = 17
"""
"""
def poly_eval(p, x):
    power = []
    mult_result = []
    def x_powers():
        power_of = list(range(len(p)))
        power = list(map(lambda a: x ** a, power_of))
        print(power)
        return power
    def mult():
        x_powers()
        mult_result = list(map(lambda a,b: a*b, power,p))
        print(mult_result)
        return mult_result
    def add():
        mult()
        final_result = reduce(lambda a,b: a+b, mult_result)
        print(final_result)
        return final_result
    add()
"""

def poly_eval(p, x):
    power_of = list(range(len(p)))
    power = list(map(lambda a: x ** a, power_of))
    #print(power)

    mult_result = list(map(lambda a, b: a * b, power, p))
    #print(mult_result)

    final_result = reduce(lambda a,b: a+b, mult_result)
    print(f"Final result is {final_result}")
    

poly_eval([1,2,3,4,5,6,7,8,9,10],5)
