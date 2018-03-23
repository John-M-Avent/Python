def verbs(verb):
    ### Converts a first-person singular verb into a third-person sigular verb.###
    VerbList = list(verb)               # Converts the verb into a list of its letters. 
    LastLetter = VerbList.pop()         # Pops the last letter of the list. 
    if LastLetter == 'y':               # If the last letter is y...
        VerbList.append('ies')          # Adds 'ies' to the verb list. 
    elif LastLetter == 'o' or LastLetter == 'h' or LastLetter == 's' or LastLetter == 'x' or LastLetter == 'z': # If the last letter is any of those... 
        VerbList.append(LastLetter)     # Adds back the last letter. 
        VerbList.append('es')           # Adds 'es' to the verb letter list. 
    else:                               # Else... 
        VerbList.append(LastLetter)     # Adds back the last letter. 
        VerbList.append('s')            # Adds an 's' to the verb letter list. 
    VerbFinished = "".join(VerbList)    # Joins the list of letters together into one string. 
    print(VerbFinished)                 # Prints the final product. 
