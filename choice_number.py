#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 19:20:23 2021

@author: estebangracialeon
"""

import random

#Asking the user if he wants to play
start = input("Want to play: ")

#Creating a variable with a number that the user has to guess
value = random.randint(1, 9)

count = 0 #Creating a counter with 0 that is going to be used later in the while loop

#When user type yes the game start, also the loop
while start == "yes":
    #Asking the user which number he thinks is the correct answer
    guess = int(input("What number you think it is: "))
    count += 1 #each time there is a new round the counter increases +1
    if guess < value:
        print("Too low")
        guess = int(input("Try again: ")) 
    elif guess > value:
        print("Too high")
        guess = int(input("Try again: "))
    elif guess == value:
        print("Correct it took you ", count, " times")
        break 