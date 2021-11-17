#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 11:42:00 2021

@author: estebangracialeon
"""

user_input = input("Type a word to see if its a palindrome or not: ").lower()

backwards = user_input[::-1]

if user_input == backwards:
    print(user_input + " is a palindrome")
else:
    print(user_input + " is not a palindrome") 


def palindromo(palabra):
    backwards_palabra = palabra[::-1]
    if backwards_palabra == palabra:
        print(user_input + " is a palindrome")
    else:
        print(user_input + " is not a palindrome")
        

palindromo(user_input)