import random
import time
import os

#read file and create an array with words
textFile = open("words.txt", "r")
listOfWords2 = textFile.read().splitlines()
textFile.close()

for i in range(len(listOfWords2)):
    listOfWords2[i] = listOfWords2[i].lower()

MAXREACH = 6
STATUSOFGAME = 0
RESULT = 0
state = 0
run = True
underscoreAr = []
givenWord = []
randomWord = random.choice(listOfWords2)
underscores = len(randomWord)

#def hint(word):
#    print(wikipedia.summary(word))


def printWord(underscoreAr):
    for i in range(len(underscoreAr)):
        print(underscoreAr[i] + " ", end = '')


def userInput():
    #first char of the sentence
    userInput = input("Provide the character in the range A-Z   ")[0].lower()
    return userInput


def check(random, state, arr, MAXREACH):
    status, toReach = 0, len(random)
    while state != MAXREACH:
        #if state == 5:
        #    decisionHint = input("Would you like to get an hint?")
        #    if decisionHint in ["yes", "y"]:
        #        hint(random)
        uInput = userInput()
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