#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 15:53:34 2021

@author: estebangracialeon
"""
#Asking the user if he wants to play
game = (input("Do you want to play yes, no: ")).lower()
 
#Rules
# #Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random

#Creating a function to compare two values player1 and player2.
def comparation(player_1, player_2):
    if player_1 == player_2: 
        print(player_1, " and " , player_2, "it is a tie")
    elif player_1 == "rock" and player_2 == "paper":
        print("Paper beats rock, player 2 wins", )
    elif player_1 == "rock" and player_2 == "scissors":
        print("Rock beat sicssors, player 1 wins")
    elif player_1 == "paper" and player_2 == "rock":
        print("Paper beats rock , player 1 wins")
    elif player_1 == "paper" and player_2 == "scissors": 
        print("Scissors beats paper, player 2 wins")
    elif player_1 == "scissors" and player_2 == "rock":
        print("Rock beat scissors, player 2 wins")
    elif player_1 == "scissors" and player_2 == "paper":
        print("Scissors beats paper, player 1 wins")


#While loop used to initiate the game if yes the game starts, if not not starts 
while game == "yes": 
    player_1 = input("Player 1: What do you choose: Rock /Paper  /Sissors : ").lower() #asking the user an input and convert it to lower
    while player_1 != "rock" and  player_1 != "paper" and  player_1 !="scissors": #if the player writes something different than rock paper scissors this while loop starts
        if player_1 != "rock" or player_1 != "paper" or player_1 != "scissors": #While the user misspelled, and the word is still different than rock paper scissors
            player_1 = input("You misspelled write again, please: ") #We ask the user to write again till is player_1 = "rock" or "paper" or "scissors"
    choices = ["rock", "paper", "scissors"] #Creating a list with choices of the second player
    player_2 = (random.choice(choices)) #The machine picks a random choice
    print("The machine has selected", player_2) #Showing what the machine selected
    print(comparation(player_1,player_2)) #printing the result of the function
    game = input("Play again?  yes, no : ")  #we ask the user ifhe wants to start the game again, if game == "yes" then it will start again