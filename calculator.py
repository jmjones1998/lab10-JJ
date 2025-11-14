"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#https://github.com/jmjones1998/lab10-JJ.git
#Partner 1 and 2: Julia Jones

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError as e:
        raise e

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        raise e

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    return a/b

def logarithm(a,b):
    if a<= 0 or b<= 0 or b == 1:
        raise ZeroDivisionError
    return math.log(a,b)

def exp(a,b):
    return a**b