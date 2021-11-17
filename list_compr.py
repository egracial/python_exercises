# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Fri Nov 12 12:46:08 2021

# @author: estebangracialeon
# """

# #See which numbers are the same in both lists eliminating duplicates
# a =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# same_numbers = [] #Creating an empty list where we are going to store same values

# for i in a:  #Recorro todos los values en lista a
#     if i not in same_numbers and i in b: # revisar si alguno de los valores no está en la same_numbers list y está en la lista b, meterlo en same_numbers list
#         same_numbers.append(i) #incluir valores a lista same_numbers

# print(same_numbers)

# same = [i for i in b]

# suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
# numbers = [2,3,4,5,6,7,8,9,10, "Jack", "Queen", "King", "Ace"]



# deck_comprend = [(suit, number) for suit in suits for number in numbers] 

# deck = []

# for suit in suits:
#     for number in numbers:
#         card = suit, str(number)
#         deck.append(card)

# import random

# def random_lists(number_lists): #Creo función para crear varias listas con numeros diferentes pero con el mismo rango
#     lista_de_listas = [] #Creo objeto lista vacía para llenar con listas, es una lista de listas
#     for _ in range(0,number_lists): #Hago un loop y en cada ronda se va a crear una lista, dada por el argumento de la función, el underscore es porque no uso ese valor solo lo necesito para el loop
#         random_lista = [] #Creo mi lista vacía para llenar con numeros random
#         for _ in range(0,10): #Creo un rango que determina el número de valores que quiero en mi lista, en este caso, 10
#             n = random.randint(1,100) #Creo una variable interger entre 1 y 100
#             random_lista.append(n) #Meto la variable en la random_lista
#         lista_de_listas.append(random_lista) #Cuando el loop se acabe (0,10) meto la random_list en en la lista de listas
#     print(lista_de_listas) #imprimo lista de listas = lista_de_listas = [[lista_1],...,[lista (dependiendo el number of lists de la función)]
#     return lista_de_listas #Si quiero hacer algo con mi lista de listas, devuelvo lo que se calculó

# #Testing 
# listas = random_lists(2) #Creating an object with the return values of the function random_lists
# lista_1 = listas[0]#Slice the first list
# lista_2 = listas[1]#Slice the second list

# same_values = []

# for i in lista_1:
#     if i in lista_2:
#         same_values.append(i) 
        

# #Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# list_to_work = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# free = []

# for i in list_to_work: 
#     residual = i % 2
#     if residual != 1:
#         free.append(i)


# free_comprehension = [i for i in list_to_work if i%2 != 1]


# a =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# same_numbers = [] #Creating an empty list where we are going to store same values

# for i in a:  #Recorro todos los values en lista a
#     if i not in same_numbers and i in b: # revisar si alguno de los valores no está en la same_numbers list y está en la lista b, meterlo en same_numbers list
#         same_numbers.append(i) #incluir valores a lista same_numbers

# print(same_numbers)


# equal_values = [i for i in a if i in b]



# dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

# #Type your answer here.

# lst=[i.upper() for i in dict.keys() if dict[i]  < 5000]

# vehicles_less_5000 = []

# for i in dict.keys():
#     if dict[i] > 5000:
#         vehicles_less_5000.append(i)


# print(lst)


# def random_lists(number_lists): #Creo función para crear varias listas con numeros diferentes pero con el mismo rango
#     lista_de_listas = [] #Creo objeto lista vacía para llenar con listas, es una lista de listas
#     for _ in range(0,number_lists): #Hago un loop y en cada ronda se va a crear una lista, dada por el argumento de la función, el underscore es porque no uso ese valor solo lo necesito para el loop
#         random_lista = [] #Creo mi lista vacía para llenar con numeros random
#         for _ in range(0,10): #Creo un rango que determina el número de valores que quiero en mi lista, en este caso, 10
#             n = random.randint(1,100) #Creo una variable interger entre 1 y 100
#             random_lista.append(n) #Meto la variable en la random_lista
#         lista_de_listas.append(random_lista) #Cuando el loop se acabe (0,10) meto la random_list en en la lista de listas
#     print(lista_de_listas) #imprimo lista de listas = lista_de_listas = [[lista_1],...,[lista (dependiendo el number of lists de la función)]
#     return lista_de_listas



import random

#Creating a function with different attributes max_value on intergers, length of list, and number of list we want
#This function give us a list of lists
def comprehension_lists(max_value, lenght_of_list_entry, number_of_lists):
    return[[random.randint(1,max_value) for i in range(0,lenght_of_list_entry)]for i in range(0, number_of_lists)]


#Creating a list of lists that returns the result of the function to use it later
aprendiendo_listas = comprehension_lists(100,10, 4) 

#Creating a list that is going to store what we need
same_values = []

#Looking for same values in all lists, if there is, append them in the new list 
for j in aprendiendo_listas[0]: 
    if j in aprendiendo_listas[1] or j in aprendiendo_listas[2] or j in aprendiendo_listas[3]: 
        same_values.append(j)
for k in aprendiendo_listas[1]:
    if k in aprendiendo_listas[2] or k in aprendiendo_listas[3]: 
        same_values.append(k)
for l in aprendiendo_listas[2]:
    if l in aprendiendo_listas[3]: 
        same_values.append(l)



print(aprendiendo_listas)
print(same_values)









