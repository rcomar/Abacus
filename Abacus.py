import os
import math
import time

def print_title_screen():
    os.system('clear')
    print("\t************************************")
    print("\t************  ABACUS  **************")
    print("\t************************************")

def get_number():
    inputData = input("\nPlease write a number between 0 and 9999: ")
    if inputData.isnumeric():
       return int(inputData)

def print_Abacus(numb : int):
    print_title_screen()  
    length = 1
    if (numb != 0 ):
        length = int(math.log10(numb) + 1)
    print("Number: " + str(numb))
    for x in range (0,4):
        numbAux = int(numb / (math.pow(10,x + 1)))
        numbAux = int(numb - (numbAux * math.pow(10, x + 1)))
        if (x > 0):
            numbAux = int(numbAux / pow(10,x))         
        print("- |", end="")
        for y in range(0, 10- numbAux):            
            print("x",end="")
        for z in range(0,5):
            print("-",end="")
        for aa in range(0, numbAux):
            print("x",end="")
        print("|",end="")
        print(" -")
            
print_title_screen()
numb = -1
while numb != -2:      
    numb = get_number()    
    if numb >= 0 and numb <= 9999:
        print_Abacus(numb)
    else:        
        print_title_screen()  
        print("Bad input!")