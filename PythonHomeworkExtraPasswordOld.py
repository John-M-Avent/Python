## Python Homework Extra: Password Generater 
# John M. Avent 
# ENG 101-06 
# 5/1/2017 
# 
# Setup
# 
import random                                                                       # Imports the random functions.
from random import shuffle                                                          # Imports shuffle from random. 
import string                                                                       # Imports string. 
Uppercase = string.ascii_uppercase                                                  # } 
Lowercase = string.ascii_lowercase                                                  # } Imports the lists of uppercase and lowercase letters, 
Numbers = string.digits                                                             # } numbers, and characters. 
Characters = string.punctuation                                                     # } 
UppercaseList = list(Uppercase)                                                     # ]
LowercaseList = list(Lowercase)                                                     # ] Turn the lists into lists, i.e., breaks the things inside into
NumbersList = list(Numbers)                                                         # ] their compenants. (This may not be necsessary)
CharactersList = list(Characters)                                                   # ]
ListAll = UppercaseList + LowercaseList + NumbersList + CharactersList              # Adds all the lists together. 
UppercaseLength = len(UppercaseList)                                                # }
LowercaseLength = len(LowercaseList)                                                # } Takes the length of each list. 
NumbersLength = len(NumbersList)                                                    # }
CharactersLength = len(CharactersList)                                              # }
UppercaseNeeded = 0                                                                 # ]
LowercaseNeeded = 0                                                                 # ] Sets up variables for later use. 
NumbersNeeded = 0                                                                   # ]
CharactersNeeded = 0                                                                # ]
UppercaseChosen = []                                                                # }
LowercaseChosen = []                                                                # } Sets up lists for the chosen items to be added to. 
NumbersChosen = []                                                                  # }
CharactersChosen = []                                                               # }
UppercaseRun = 1                                                                    # ]
LowercaseRun = 0                                                                    # ] Sets up variables for the 'while' loops to run off of. 
NumbersRun = 0                                                                      # ]
CharactersRun = 0                                                                   # ]
#
# Uppercase Letters 
# 
while UppercaseRun == 1:                                                            # Runs the 'while' loop. 
    UppercaseNeeded = input("Enter the number of uppercase letters needed: ")       # Queries the user for the number they want. 
    UppercaseCheck = 0                                                              # }
    for Number in Numbers:                                                          # }
        for Item in UppercaseNeeded:                                                # } Checks if the input is a number. 
            if Number == Item:                                                      # }
                UppercaseCheck = 1                                                  # }
    if UppercaseCheck == 1:                                                         # If it is a number... 
        UppercaseGenerated = 0                                                      # Initializes the number generated. 
        while UppercaseGenerated < int(UppercaseNeeded):                            # While the number of things generated is less than the number required. 
            UppercaseNumber = random.randint(0, UppercaseLength -1)                 # Generates a random number. 
            UppercaseLetter = UppercaseList[UppercaseNumber]                        # Converts the random number into the random item required. 
            UppercaseChosen.append(UppercaseLetter)                                 # Adds the random item to its list. 
            UppercaseGenerated += 1                                                 # Adds one to the number generated. 
        if UppercaseGenerated == int(UppercaseNeeded):                              # If the number generated is the same as the number needed... 
            LowercaseRun = 1                                                        # Sets up for the next 'while' loop. 
            break                                                                   # Breaks the 'while' loop. 
    else:                                                                           # Else... 
        print ("Enter a number please (i.e. 1, 5 79842987): ")                      # Prints an error message. 
#
# Lowercase Letters 
# 
while LowercaseRun == 1:                                                            # Runs the 'while' loop. 
    LowercaseNeeded = input("Enter the number of lowercase letters needed: ")       # Queries the user for the number they want. 
    LowercaseCheck = 0                                                              # } 
    for Number in Numbers:                                                          # } 
        for Item in LowercaseNeeded:                                                # } Checks if the input is a number. 
            if Number == Item:                                                      # } 
                LowercaseCheck = 1                                                  # } 
    if LowercaseCheck == 1:                                                         # If it is a number... 
        LowercaseGenerated = 0                                                      # Initializes the number generated. 
        while LowercaseGenerated < int(LowercaseNeeded):                            # While the number of things generated is less than the number required. 
            LowercaseNumber = random.randint(0, LowercaseLength - 1)                # Generates a random number. 
            LowercaseLetter = LowercaseList[LowercaseNumber]                        # Converts the random number into the random item required. 
            LowercaseChosen.append(LowercaseLetter)                                 # Adds the random item to its list. 
            LowercaseGenerated += 1                                                 # Adds one to the number generated. 
        if LowercaseGenerated == int(LowercaseNeeded):                              # If the number generated is the same as the number needed... 
            NumbersRun = 1                                                          # Sets up for the next 'while' loop. 
            break                                                                   # Breaks the 'while' loop. 
    else:                                                                           # Else... 
        print ("Enter a number please (i.e. 1, 5 79842987): ")                      # Prints an error message. 
#
# Numbers 
# 
while NumbersRun == 1:                                                              # Runs the 'while' loop. 
    NumbersNeeded = input("Enter the number of numbers needed: ")                   # Queries the user for the number they want. 
    NumbersCheck = 0                                                                # }
    for Number in Numbers:                                                          # }
        for Item in NumbersNeeded:                                                  # } Checks if the input is a number. 
            if Number == Item:                                                      # }
                NumbersCheck = 1                                                    # }
    if NumbersCheck == 1:                                                           # If it is a number... 
        NumbersGenerated = 0                                                        # Initializes the number generated. 
        while NumbersGenerated < int(NumbersNeeded):                                # While the number of things generated is less than the number required. 
            NumbersNumber = random.randint(0, NumbersLength - 1)                    # Generates a random number. 
            NumbersLetter = NumbersList[NumbersNumber]                              # Converts the random number into the random item required. 
            NumbersChosen.append(NumbersLetter)                                     # Adds the random item to its list. 
            NumbersGenerated += 1                                                   # Adds one to the number generated. 
        if NumbersGenerated == int(NumbersNeeded):                                  # If the number generated is the same as the number needed... 
            CharactersRun = 1                                                       # Sets up for the next 'while' loop. 
            break                                                                   # Breaks the 'while' loop. 
    else:                                                                           # Else... 
        print ("Enter a number please (i.e. 1, 5 79842987): ")                      # Prints an error message. 
#
# Characters 
# 
while CharactersRun == 1:                                                           # Runs the 'while' loop. 
    CharactersNeeded = input("Enter the number of special characters needed: ")     # Queries the user for the number they want. 
    CharactersCheck = 0                                                             # }
    for Number in Numbers:                                                          # }
        for Item in CharactersNeeded:                                               # } Checks if the input is a number. 
            if Number == Item:                                                      # }
                CharactersCheck = 1                                                 # }
    if CharactersCheck == 1:                                                        # If it is a number... 
        CharactersGenerated = 0                                                     # Initializes the number generated. 
        while CharactersGenerated < int(CharactersNeeded):                          # While the number of things generated is less than the number required. 
            CharactersNumber = random.randint(0, CharactersLength - 1)              # Generates a random number. 
            CharactersLetter = CharactersList[CharactersNumber]                     # Converts the random number into the random item required. 
            CharactersChosen.append(CharactersLetter)                               # Adds the random item to its list. 
            CharactersGenerated += 1                                                # Adds one to the number generated. 
        if UppercaseGenerated == int(UppercaseNeeded):                              # If the number generated is the same as the number needed... 
            break                                                                   # Breaks the 'while' loop. 
    else:                                                                           # Else... 
        print ("Enter a number please (i.e. 1, 5 79842987): ")                      # Prints an error message. 
#
# Password Generation 
#
AllChosen = UppercaseChosen + LowercaseChosen + NumbersChosen + CharactersChosen    # Adds the lists of chosen items together. 
shuffle(AllChosen)                                                                  # Randomizes the list. 
Password = "".join(AllChosen)                                                       # Adds the items into one string. 
print(Password)                                                                     # Prints the string. 
