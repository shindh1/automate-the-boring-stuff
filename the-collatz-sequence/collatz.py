# collatz.py
# Author: Daniel Shin
# Source: Automate the Boring Stuff with Python Ch. 3 Practice Project (p77)

import sys

while True:
    inputNumber = input("Enter a number: ")
    try:
        number = int(inputNumber)
        break
    except ValueError:
        print('Error: You must enter an intenger')
        continue
    
def collatz(number):
    while number != 1:
        if number % 2 == 1:
            number = 3 * number + 1
            print(str(number))
        else:
            number = number // 2
            print(str(number))

collatz(number)
            
    
