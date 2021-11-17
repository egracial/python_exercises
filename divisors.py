#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 12:12:45 2021

@author: estebangracialeon
"""
#Ask the user a number and convert it to interger
number = int(input("What is the number: "))

#Divide the number to all numbers smaller than that

#Create a list of all numbers to divide the one
x = range(1,(number+1))


# Creating the empty list we are going to fill
divisors =[]

for i in x: #Loop all numbers between 1 and the number given by the user
    division = number % i #See if there is a residual in the division 
    if division == 0: #If there is not residual
        divisors.append(i) #Append that number to the list

print(divisors)