# John M. Avent
# Python Seminar Code
# Created 3-23-2018
#
# This code is an example of a menu with function backend
#
# Intro, Imports, and Other Setup Stuff
import random

# Prints header of program
print("\n ____________________________________")
print(" Welcome to the program. ")
print(" At any point, type 'exit' to exit. ")
print(" ____________________________________")

#
# The Loop
#
Loop_Control_Variable = 1                   # This is the variable that runs The Loop

while Loop_Control_Variable == 1:           # The program runs via this loop
    #
    # Menu Header
    #
    print("\n ____________________________________")
    print(" Below are the numbered menu options.")
    print(" 1)   :   Instructions")
    print(" 2)   :   Roll Some Dice")
    print(" 3)   :   ")
    print(" 4)   :   ")
    print(" 5)   :   ")
    print(" 6)   :   ")
    print(" 7)   :   ")
    print(" 8)   :   ")
    print(" 9)   :   ")
    print(" 0)   :   Exit")
    print(" ____________________________________")
    #
    Menu_Input = input(" Enter a number to select an option: ") # Meny option Select
    #
    # These if Statement determine which option was selected from the menu
    #
    if Menu_Input == "exit":                # The user has elected to exit the program
        print(" Thank you for running this program.")
        print(" ____________________________________\n")
        Loop_Control_Variable = 0           # This ends The Loop
    #
    elif Menu_Input == "1":                 # 1: Instructions Option selected.
        print("\n Enter a number to select an option of off the menu.")
        print(" At any point, type 'exit' to exit the whole program.")
    #
    elif Menu_Input == "2":                 # 2: Roll Some Dice selected
        # Roll Some Dice Header
        print("\n ____________________________________")
        print(" Here you can simulater rolling dice.")
        Number_of_Dice = input(" Enter the number of dice to roll: ")
        # Input Evaluation
        if Number_of_Dice.lower() == 'exit':    # Exits entire program
            print("\n Thank you for running this program.")
            print(" ____________________________________\n")
            Loop_Control_Variable = 0
        else:                               # Outputs
            Number_of_Dice = int(Number_of_Dice)
            Roll = random.randint(Number_of_Dice, Number_of_Dice*6) # Generates a random
                                                # from each dices equals 1 to each equal 6.
            print("\n The result is " + str(Roll) + " for " + str(Number_of_Dice) + " dice rolled.")
    #
    elif Menu_Input == "3":
        a = 1
    #
    elif Menu_Input == "4":
        a = 1
    #
    elif Menu_Input == "5":
        a = 1
    #
    elif Menu_Input == "6":
        a = 1
    #
    elif Menu_Input == "7":
        a = 1
    #
    elif Menu_Input == "8":
        a = 1
    #
    elif Menu_Input == "9":
        a = 1
    #
    elif Menu_Input == "0":                 # 0: Exit selected
        # Prints exit message
        print("\n Thank you for running this program.")
        print(" ____________________________________\n")
        Loop_Control_Variable = 0
    #
    else:                   # If the user entered something not on the list
        print(" Please enter an option listed on the menu.")
#99 Red Baloons/ 99 Luft Baloon
