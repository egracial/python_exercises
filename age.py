#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:47:34 2021

@author: estebangracialeon
"""

'''#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button) '''
                                                                       
#Variables to user
name = input("What is your name: ")
age = int(input("What is your age: "))

#Year that is going to be given to the user
year_100 = str(2021 - age + 100)

#Message to the user
message = print("Hello "+ name + " you will turn 100 years old in " + year_100 + "\n") 

#Times to repeat the message
times= int(input("Choose a number to reapeat : "))

#Printing the times the person has chosen
for i in range(0, times ):
    print("Hello "+ name + " you will turn 100 years old in " + year_100 + "\n")
 