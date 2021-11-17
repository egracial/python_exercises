#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 12:35:59 2021

@author: estebangracialeon
"""
#See which numbers are the same in both lists eliminating duplicates
a =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

same_numbers = [] #Creating an empty list where we are going to store same values

for i in a:  #Recorro todos los values en lista a
    if i not in same_numbers and i in b: # revisar si alguno de los valores no está en la same_numbers list y está en la lista b, meterlo en same_numbers list
        same_numbers.append(i) #incluir valores a lista same_numbers

print(same_numbers)

#Randomly generate two lists to test this
import random

#List to fill
list_1 = []
list_2 = []

#For loop of the number of numbers we want on the list
for i in range(0,29): #10 numbers on the list
    n = random.randint(1, 200)#The randon numbers to put on the list 1
    m = random.randint(1, 200)#The randon numbers to put on the list 2
    list_1.append(n)#Appending the numbers to the list 1
    list_2.append(m)#Appending the numbers to the list 2
    
for i in list_1:
    if i in list_2:
        print(i)

#Using functions to create a number of list with random values

def random_lists(number_lists): #Creo función para crear varias listas con numeros diferentes pero con el mismo rango
    lista_de_listas = [] #Creo objeto lista vacía para llenar con listas, es una lista de listas
    for _ in range(0,number_lists): #Hago un loop y en cada ronda se va a crear una lista, dada por el argumento de la función, el underscore es porque no uso ese valor solo lo necesito para el loop
        random_lista = [] #Creo mi lista vacía para llenar con numeros random
        for _ in range(0,10): #Creo un rango que determina el número de valores que quiero en mi lista, en este caso, 10
            n = random.randint(1,100) #Creo una variable interger entre 1 y 100
            random_lista.append(n) #Meto la variable en la random_lista
        lista_de_listas.append(random_lista) #Cuando el loop se acabe (0,10) meto la random_list en en la lista de listas
    print(lista_de_listas) #imprimo lista de listas = lista_de_listas = [[lista_1],...,[lista (dependiendo el number of lists de la función)]
    return lista_de_listas #Si quiero hacer algo con mi lista de listas, devuelvo lo que se calculó

#Testing 
listas = random_lists(2) 
lista_1 = listas[0]
lista_2 = listas[1]

same_values = []

for i in lista_1:
    if i in lista_2:
        same_values.append(i) 