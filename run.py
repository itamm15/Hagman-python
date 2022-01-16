from pickletools import uint1
#import wikipedia
#from functions import *
import random 
import time
import os
from re import S



#read file and create an array with words
textFile = open("words.txt", "r")
listOfWords2 = textFile.read().splitlines()
textFile.close()

for i in range(len(listOfWords2)):
    listOfWords2[i] = listOfWords2[i].lower()

#GLOBAL VARIABLES
MAXREACH = 6
STATUSOFGAME = 0
RESULT = 0
state = 0
run = True
underscoreAr = []
givenWord = []
lettersProvided = []
randomWord = random.choice(listOfWords2)
underscores = len(randomWord)

#FUNCTIONS 

#def hint(word):
#    print(wikipedia.summary(word))

#def to check, whether the user provided the same character again

def isProvided(lettersProvided, uInput):
    if uInput in lettersProvided:
        return True
    return False


def printWord(underscoreAr):
    for i in range(len(underscoreAr)):
        print(underscoreAr[i] + " ", end = '')


def userInput():
    #first char of the sentence
    userInput = input("Provide the character in the range A-Z   ")[0].lower()
    clear()
    return userInput


def check(random, state, arr, MAXREACH):
    status, toReach = 0, len(random)
    while state != MAXREACH:
        #if state == 5:
        #    decisionHint = input("Would you like to get an hint?")
        #    if decisionHint in ["yes", "y"]:
        #        hint(random)
        uInput = userInput()
        if isProvided(lettersProvided, uInput):
            print("You have already provided the ", uInput, "!")
            uInput = userInput()
            clear()
            while uInput in lettersProvided:
                print("You have already provided the ", uInput, "!")
                uInput = userInput()
                clear()
        lettersProvided.append(uInput)
        checker = False
        for i in range(len(random)):
            if uInput == random[i]:
                arr[i] = uInput
                checker = True
                status += 1
            if status == toReach:
                #print("Well done!")
                #remember about semicolon
                return True
        printWord(arr)
        if checker != True:
            state += 1
            clear()
            print(state, " mistake!")
    if state == MAXREACH:
        return False
   
def randomToArray(randomWord):
    for i in randomWord:
        givenWord.append(i)



def toUnderscore(underscore):
    for i in range(underscores):
        underscoreAr.append('_')


def clear():
    command = 'clear'
    #check, wheter the system is windows or other
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def start(STATUSOFGAME):
    if STATUSOFGAME == 0:
        print("Welcome in the Hangman game! You will be given a random word, and you have to guess it. Good luck!")
        time.sleep(3)
        clear()

def bye():
    print("Have a nice day!")


randomToArray(randomWord)
toUnderscore(underscoreAr)


#MAIN LOOP
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
            lettersProvided = []
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
            lettersProvided = []
            randomWord = random.choice(listOfWords2)
            underscores = len(randomWord)
            randomToArray(randomWord)
            toUnderscore(underscoreAr)
            clear()





