def password(UppercaseNeeded,LowercaseNeeded,NumbersNeeded,CharactersNeeded):
    ### Generates a random password based on the number of characters required by each input.###
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
    while UppercaseRun == 1:                                                        # Runs the 'while' loop
        UppercaseGenerated = 0                                                      # Initializes the number generated. 
        while UppercaseGenerated < int(UppercaseNeeded):                            # While the number of things generated is less than the number required. 
            UppercaseNumber = random.randint(0, UppercaseLength -1)                 # Generates a random number. 
            UppercaseLetter = UppercaseList[UppercaseNumber]                        # Converts the random number into the random item required. 
            UppercaseChosen.append(UppercaseLetter)                                 # Adds the random item to its list. 
            UppercaseGenerated += 1                                                 # Adds one to the number generated.
        if UppercaseGenerated == int(UppercaseNeeded):                              # If the number generated is the same as the number needed... 
            LowercaseRun = 1                                                        # Sets up for the next 'while' loop. 
            break                                                                   # Breaks the 'while' loop. 
    #
    # Lowercase Letters 
    #
    while LowercaseRun == 1:                                                        # Runs the 'while' loop.
        LowercaseGenerated = 0                                                      # Initializes the number generated. 
        while LowercaseGenerated < int(LowercaseNeeded):                            # While the number of things generated is less than the number required. 
            LowercaseNumber = random.randint(0, LowercaseLength - 1)                # Generates a random number. 
            LowercaseLetter = LowercaseList[LowercaseNumber]                        # Converts the random number into the random item required. 
            LowercaseChosen.append(LowercaseLetter)                                 # Adds the random item to its list. 
            LowercaseGenerated += 1                                                 # Adds one to the number generated. 
        if LowercaseGenerated == int(LowercaseNeeded):                              # If the number generated is the same as the number needed... 
            NumbersRun = 1                                                          # Sets up for the next 'while' loop. 
            break                                                                   # Breaks the 'while' loop. 
    #
    # Numbers 
    # 
    while NumbersRun == 1:                                                          # Runs the 'while' loop.
        NumbersGenerated = 0                                                        # Initializes the number generated. 
        while NumbersGenerated < int(NumbersNeeded):                                # While the number of things generated is less than the number required. 
            NumbersNumber = random.randint(0, NumbersLength - 1)                    # Generates a random number. 
            NumbersLetter = NumbersList[NumbersNumber]                              # Converts the random number into the random item required. 
            NumbersChosen.append(NumbersLetter)                                     # Adds the random item to its list. 
            NumbersGenerated += 1                                                   # Adds one to the number generated. 
        if NumbersGenerated == int(NumbersNeeded):                                  # If the number generated is the same as the number needed... 
            CharactersRun = 1                                                       # Sets up for the next 'while' loop. 
            break                                                                   # Breaks the 'while' loop. 
    #
    # Characters 
    # 
    while CharactersRun == 1:                                                       # Runs the 'while' loop. 
        CharactersGenerated = 0                                                     # Initializes the number generated. 
        while CharactersGenerated < int(CharactersNeeded):                          # While the number of things generated is less than the number required. 
            CharactersNumber = random.randint(0, CharactersLength - 1)              # Generates a random number. 
            CharactersLetter = CharactersList[CharactersNumber]                     # Converts the random number into the random item required. 
            CharactersChosen.append(CharactersLetter)                               # Adds the random item to its list. 
            CharactersGenerated += 1                                                # Adds one to the number generated. 
        if UppercaseGenerated == int(UppercaseNeeded):                              # If the number generated is the same as the number needed... 
            break                                                                   # Breaks the 'while' loop. 
    #
    # Password Generation 
    #
    AllChosen = UppercaseChosen + LowercaseChosen + NumbersChosen + CharactersChosen    # Adds the lists of chosen items together. 
    shuffle(AllChosen)                                                                  # Randomizes the list. 
    Password = "".join(AllChosen)                                                       # Adds the items into one string. 
    print(Password)                                                                     # Prints the string. 
