#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:52:31 2021

@author: estebangracialeon
"""

#Ask for a number 
number = int(input("What number you choose: "))

#Looking for the residuals
number_residual_4 = number % 4
number_residual_2 = number % 2

#Seeing if number is odd or even
'''
if number_residual_2 == number_residual_4:
    print(str(number)+ "is multiple of 4 and 2")
elif number_residual_4 == 0:
    print(str(number) + " is multiple of 4")
elif number_residual_2 == 0: 
    print(str(number)+ " is multiple of 2")
else:
    print(str(number) + " is even") 
    '''
    
#Asking the user if num divides evenly 
key = int(input("What is the key: "))

number_residual = number % key

#Condition to know if is or not divided evenly
if number_residual == 0:
    print( number, " divides evenly in", key)
else:
    print(number, " does not divides evenlty with ", key)