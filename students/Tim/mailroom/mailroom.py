# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:45:27 2019

@author: tdietz
"""
import sys
donorList = [("Elon Musk", [45643.05, 60029090.04]), 
             ("Hank Hill",[23.00, 457.47]), 
             ("Wade Watts", [430594.56, 420.69]),
             ("Stan Lee", [345698.45, 3490938.56]),
             ("Col Mustard", [4345.45, 3434.46]),
             ("Mark Normand", [45.00]),
            ]

def createReport():
    print("Create Report Option")
    #TODO create a function that generates a report
    
    quitToMain()

def sendThankYou():
    nameOfPerson = input("Please enter a name (First Last): ")
    if nameOfPerson in donorList:
        print("TODO")
    elif nameOfPerson.lower() == 'list':
        for key in donorList:
            print(key)
            sendThankYou() #repromt the please enter a name
    else:
        donorList.append(nameOfPerson,[])
        
    
    
    quitToMain()    
    #TODO create a function that automates a thank you email

#function to exit program or return to main menu
def quitToMain():
    userInput = input("Would you like to return to the main menu? (y/n): ")
    while userInput != 'y' or 'n':       
        if userInput == 'n':
            quitProgram()
        elif userInput == 'y':
            return
        else:
            print("Please choose valid input")
            userInput = input("Would you like to return to the main menu? (y/n): ")
#Function to quit program
def quitProgram():
    print("Good Bye")
    sys.exit(0)

#Funtion displaying user menu
def userMenu():
    print("\nWhat would you like to do?")
    print("1: Create Report")
    print("2: Send Thank You")
    print("3: Quit")

#Main function to run the program
def main():
    while True:
        userMenu()
        userResponse = input("Please choose: ")
        if userResponse == "1":
            createReport()
        elif userResponse == "2":
            sendThankYou()
        elif userResponse == "3":
            quitProgram()
            
        
        
if __name__ == '__main__':
    main()
    