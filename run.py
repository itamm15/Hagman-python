from pickletools import uint1
#import wikipedia
from functions import *
import random 
import time
import os
from re import S


randomToArray(randomWord)
toUnderscore(underscoreAr)
while run:
    start(STATUSOFGAME)
    printWord(underscoreAr)
    #print(givenWord)
    victory = check(randomWord, state, underscoreAr, MAXREACH)
    STATUSOFGAME += 1
    clear()
    if victory:
        RESULT += 1
        print("You won! Your result is ", RESULT,  ". The world was ", randomWord.upper(), ". Wanna play again?")
        decision = input("[Yes/No]")
        if decision in ['yes','y']:
            run = True
            underscoreAr = []
            randomWord = random.choice(listOfWords2)
            underscores = len(randomWord)
            randomToArray(randomWord)
            toUnderscore(underscoreAr)
            clear()
        else: 
            bye()
            run = False
    else:
        print("You lost! Wanna play again? The word was " + randomWord.upper(), ", and your result is ", RESULT)
        decision = input("[Yes/No]")
        if decision in ["no","n"]:
            bye()
            run = False
        else: 
            run = True
            underscoreAr = []
            randomWord = random.choice(listOfWords2)
            underscores = len(randomWord)
            randomToArray(randomWord)
            toUnderscore(underscoreAr)
            clear()





