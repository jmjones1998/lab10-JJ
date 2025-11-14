"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""


import math

def add(a, b): 
    return a + b

import math


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

def exp(a,b):
    return a**b


def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def logarithm(a, b):
    if a<= 0 or b <= 0 or b == 1:
        raise ZeroDivisionError

def exp(a,b):
    return a ** b
