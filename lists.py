#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:28:17 2021

@author: estebangracialeon
"""
#New list with a > 5 elements
x = []

#List given
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 

#First excercise
for i in a:
    if i >= 5:
         x.append(i) 

#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

#Ask user
number = int(input("Choose a number: "))

#List to fill with loop
new_list = []

#Loop for all elements in a that are smaller than number, append those to the new list
for i in a:
    if i <= number:
        new_list.append(i)
#Print the new list
print(new_list)
