import random
from os import system
from time import sleep


while True:
    print("what is your choice? rock, paper or scissors?\n")

    playerplays = input("player plays:    ")
    compPlays = str(random.sample(["rock", "paper", "scissors"], 1)[0])     #random.sample, mint lista 1. eleme stringé 
  
    dict = {"rock" : 0, "paper" : 1, "scissors" : 2}                        #későbbi vizsgálatokhoz számmá alakítva a választások

    try:
        x = dict[playerplays]

    except Exception:
        print("please enter a legit choice!")

    else:    
        print("computer plays:  " + compPlays)

        print("\n")

        if (int(dict[playerplays]) + 1) % 3 == int(dict[compPlays]):
            print("you lose!")

        elif (int(dict[playerplays]) - 1) % 3 == int(dict[compPlays]):
            print("you win!") 

        else:
            print("Draw")
    
    
    sleep(3)
    system("cls")
