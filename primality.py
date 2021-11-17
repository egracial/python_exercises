#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:31:45 2021

@author: estebangracialeon
"""

#Check Primality Functions

#Creating a function that says if a number is prime or not
def primality_number(number): #the function has one attribute, the number
    lista_de_divisores_enteros = [i for i in range(2,number) if number%i == 0] #Create a list of numbers  if the residual of the number divided by each number before this number(starting in two) ex: 10/2, 10/3, 10/4...etc... is 0
    if not lista_de_divisores_enteros: #If the list is empty 
        print(number, " es primo") 
    else: #If the list has some divisors that divides number enterly 
        print(number, "has this numbers as entirly divisors", lista_de_divisores_enteros)
    
primality_number(98)