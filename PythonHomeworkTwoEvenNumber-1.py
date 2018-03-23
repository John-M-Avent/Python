## Python Homework One: Even Number
# John M. Avent 
# ENG 101-06 
# 4/18/2017 
# 
# Setup 
#
Run = 1                                             # Variable for 'while' loop to run on. 
InputNumbersList = []                               # Blank list for numbers inputed. 
EvenList = []                                       # Blank list for even number. 
Numbers = "0123456789"                              # } Sets up a list of numbers. 
NumbersList = list(Numbers)                         # }
# 
# Builds the List of Numbers 
# 
while Run ==1:                                      # Runs a 'while' loop to build the list of numbers. 
    Number = input ("Enter an integer or type quit when finished: ")             # Queries the user for the number they want to add to the list. 
    InputNumberAsList = list(Number)                # Splits the input into a list of its characters. 
    NumberCheck = 0                                 # Sets the number check to false.
    if Number == 'quit' or Number == 'Quit':        # If they user wants to quit... 
        break                                       # Breaks the 'while' loop. 
    else:                                           # Else... 
        for Character in InputNumberAsList:         # Goes through the user's input one character at a time. 
            for Thing in NumbersList:               # Goes the numbers one at a time. 
                if Character == Thing:              # If the user input is a number... 
                    NumberCheck = 1                 # Number check is true.
    if NumberCheck == 1:                            # If number check is true... 
        InputNumbersList.append(Number)             # Adds the number to the list of number to be checked. s
        ItemCountRun = 0                            # Sets up to end the number 'while' loop. 
    elif NumberCheck == 0:                          # If number check is false... 
        print ("Please enter a number (i.e. 2, 17, 2345).")                     # Prints an error for the user to input a number. 
# 
# Checks the List 
#
for Item in InputNumbersList:                       # For each number inputed... 
    Item = int(Item)                                # Changes number from string to integer. 
    NumberHalf = Item/ 2                            # Divides the number in two. 
    NumberRound = round (NumberHalf)                # Round the number divded by two. 
    if Item == 1:                                   # If the number is one... 
        Nothing = 1                                 # A placeholder so one doesn't get added to the list of even numbers. 
    elif NumberHalf == NumberRound:                 # If the half the number is the same as half the number rounded, which only happens for even number unless the number is very large.. 
        EvenList.append(Item)                       # Adds the number to the list of even numbers. 
print(EvenList)                                     # Prints the list of even number. 
