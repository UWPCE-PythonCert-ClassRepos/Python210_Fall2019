# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:45:27 2019

@author: tdietz
"""
from datetime import date
import sys
donorList = {"Elon Musk": [45643.05, 60029090.04], 
             "Hank Hill":[23.00, 457.47], 
             "Wade Watts": [430594.56, 420.69],
             "Stan Lee": [345698.45, 3490938.56],
             "Col Mustard": [4345.45, 3434.46],
             "Mark Normand": [45.00],
            }

def createReport():
    print("This is the current report of", date.today(), ": ")
    print("{:<30}|{:^15}|{:^12}|{:^14}".format('Donors Name', 'Total Given', ' # of Gifts', 'Average Gift'))
    print('-'*73)    
    for donor,values in donorList.items():
        totalValue = 0
        for values in donorList[donor]:
            totalValue += values
        avgValue = totalValue/len(donorList[donor])
        numGifts = len(donorList[donor])
        print('{:<30} ${:>14.2f}{:^12} ${:>13.2f}'.format(donor, totalValue, numGifts, avgValue))
    quitToMain()

def sendThankYou():
    #checks if the name is already in the current dictionary, second is if user types in 'list', third is adding a new entry to the dictionary
    nameOfPerson = input("Please enter a name (First, Last) or type \'list\' to see the current list: ")
    if nameOfPerson in donorList:
        donationAmount = float(input("How much did %s donate?: " % nameOfPerson))
        donorList[nameOfPerson].append(donationAmount)
        print("{:s}, \n\n\tWe greatly appreciate your donation amount of ${:.2f}. \n\n Best, \n The Human Fund \n".format(nameOfPerson, donationAmount))
    elif nameOfPerson.lower() == 'list':
        print("Donors currently in list: ")
        for key in donorList:
            print(key)
        sendThankYou() #repromt the please enter a name
    else:
        donationAmount = float(input("How much did %s donate?: " % nameOfPerson))
        print("{:s}, \n\n\tWe greatly appreciate your donation amount of ${:.2f}. \n\n Best, \n The Human Fund \n".format(nameOfPerson, donationAmount))
        donorList[nameOfPerson] = [donationAmount]
        
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

#userNav dictionary    
userNav = {1: ["Send a Thank You to a single donor", sendThankYou],
       2: ["Create a Report", createReport],
       3: ["Send Letters to all donors", sendThankYou],
       4: ["Quit", quitProgram]}

#Funtion displaying user menu
def userMenu():
    print("What action would you like to do?")
    print('-'*50)
    for key, value in userNav.items():
        print("{:d} - {:s}".format(key, value[0]))
    userInput = input("Type 'list' to retrieve current donors>>: ")
    userNav.get(userInput, "Please choose a different item")
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
    