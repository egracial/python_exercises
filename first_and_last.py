#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:09:53 2021

@author: estebangracialeon
"""

import random

#Creating a function that generates a random list of intergers between 0 and 100 in a range of 10 positions
def random_list_function():
    random_list = [random.randint(0, 100) for i in range(0,10)] 
    return random_list

#Because the random list just lives in the function, we take it out to use it outside the function
random_list = random_list_function()

#We create another function which takes the argument random_list, and looks for the first and last elements fo the random_list
def first_and_last(random_list):
    first_and_last_list = [random_list[0], random_list[-1]]
    return first_and_last_list