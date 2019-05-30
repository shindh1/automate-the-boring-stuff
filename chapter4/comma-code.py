# comma-code.py
# Author: Daniel Shin
# Source: Automate the Boring Stuff with Python Ch.4 Practice Project1 (p102)

def listPrinter(yourList):
    for i in range(len(yourList)):
        if i == len(yourList)-2:
            print(str(yourList[i]), end=', and ')
        elif i == len(yourList)-1:
            print(str(yourList[i]))
        else:
            print(str(yourList[i]), end=', ') # str() included in case list includes non integer values

yourList = ['apples', 'bananas', 'tofu', 'cats']

listPrinter(yourList)
