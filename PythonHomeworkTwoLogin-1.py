## Python Homework One: Login
# John M. Avent 
# ENG 101-06 
# 4/18/2017 
# 
# Setup 
#
NameCheck = 0                                   # Sets up a variable for the user name 'while' loop to run on. 
PasswordCheck = 0                               # Sets up a variable for the password 'while' loop to run on. 
UsernameList = ["admin"]                        # Sets up a list of usernames. 
UntakenList = []                                # Sets up a list to be used later. 
LoginDirectory = {"admin" : "adminpassword"}    # Sets up the dictionary of login usernames and passwords. 
# 
# Username Check
#
print ("Welcome. You need to make a login with a usernamen and password. The username must be unique and at least six characters long.")    #Prints introduction. 
print ("Your password must be a minimum of six characters, a maximum of sixteen characters, have a lower and uppercase letters, a number, and either #, $, or @")
while NameCheck == 0:					# Runs the 'while' loop until a proper username is found.
    Username = input("Enter a username: ")		# Asks user for a potential username. 
    BrokenUsername = list(Username)			# Splits the username into a list of its letters. 
    BrokenUsernameCount = len (BrokenUsername)		# Counts the number of letters in the username.
    # 
    if Username == "quit":				# } 
        break 						# } If the user wishes to quit, breaks the 'while' loop. 
    elif Username == "Quit":				# } 
        break 						# } 
    elif BrokenUsernameCount < 6:			# If the username is less than six characters... 
        print ("Your username is too short. Please make it at least six characters.")	# Prints error to user. 
    else:						# Else... 
        for name in UsernameList:			# For each existing username... 
            if Username == name:			# If the new username equals an old one... 
                print("Sorry, that name is taken.")	# Prints error. 
            else:					# Else... 
                Untaken = name 				# } Adds the username the new username isn't to the list. 
                UntakenList.append(Untaken)		# } 
    UntakenListCount = len (UntakenList)		# Takes the length of the list of usernames the new username isn't. 
    UsernameListCount = len (UsernameList)		# Takes the length of the list of usernames that already exist. 
    if UntakenListCount == UsernameListCount:		# If there is the same number of usernames in the list of usernames that the new one isn't as there are taken usernames... 
        print ("Your username " + Username + " is unique and has been accepted.")	# Prints acceptance message. 
        NameCheck = 1 					# Marks the username 'while' loop complete. 
        UsernameList.append (Username)			# Adds the username to the list. 
        PasswordCheck = 1 				# Sets up for the password checking 'while' loop. 
        break 						# Breaks the 'while' loop. 
# 
# 
# 
LowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"		# } 
LowerCaseLettersList = list(LowerCaseLetters)		# } This sets up list of all the lower and upper case letters, numbers, and characters. 
UpperCaseLetters = LowerCaseLetters.upper()		# } 
UpperCaseLettersList = list(UpperCaseLetters)		# } I didn't need the second line that turns them into a list, but decided that would be quicker than
Numbers = "0123456789"					# } typing out the whole list manually like I did with the characters. 
NumbersList = list (Numbers)				# } 
CharactersList = ["$", "#", "@"]			# } 
# 	
# Password Checking 
#
while PasswordCheck == 1:				# Runs the password checking 'while' loop once the username 'while' loop is complete. 
    PasswordCheckLower = 0 				# } 
    PasswordCheckUpper = 0				# } Resets the checks after every failed password. 
    PasswordCheckNumber = 0				# } 
    PasswordCheckSymbol = 0				# } 
    Password = input ("Enter a password: ")		# Asks the user for a potential password. 
    PasswordLetterList = list (Password)		# Breaks the password into a list of its characters. 
    PasswordLetterLength = len (PasswordLetterList)	# Takes the length of the password. 
    if Password == "quit":				# } 
        break						# } If the user wishes to quit, breaks the 'while' loop. 
    elif Password == "Quit":				# } 
        break						# } 
    elif PasswordLetterLength < 6:			# If the password is less than 6 characters... 
        print ("Your password should be at least six characters.")	# Prints error message. 
    elif PasswordLetterLength > 16:			# If the password is longer than 16 characters...
        print ("Your password should be at most sixteen characters.")	# Prints error message. 
    else:						# Else... if all other conditions are acceptable. 
        for Item in PasswordLetterList:			# For each character in the password...
            for Unit in LowerCaseLettersList:		# For each lowercase letter... 
                if Item == Unit:			# If there is a lowercase letter in the password... 
                    PasswordCheckLower = 1		# There is a lowercase letter in the password. Test Passed! 
            for Unit in UpperCaseLettersList:		# For each uppercase letter... 
                if Item == Unit:			# If there is an uppercase letter in the password... 
                    PasswordCheckUpper = 1		# There is an uppercase letter in the password. 
            for Unit in NumbersList:			# For each number 0 through 9... 
                if Item == Unit:			# If there is a number in the password... 
                    PasswordCheckNumber = 1		# There is a number in the password. 
            for Unit in CharactersList:			# For each character... 
                if Item == Unit:			# If there is a character in the password... 
                    PasswordCheckSymbol = 1		# There is a character in the password. 
        PasswordCheckSum = PasswordCheckLower + PasswordCheckUpper + PasswordCheckNumber + PasswordCheckSymbol		# Adds the password checks together. Should equal 4 if the password is correct. 
        if PasswordCheckSum == 4:			# If the password check sum equals 4... 
            print ("Password Approved.")		# Prints acceptance message.
            PasswordCheck = 2				# Marks the password check 'while' loop complete. 
            LoginDirectory[Username] = Password		# Adds the username and password to a dictionary together. 
            break					# Breaks the password check 'while' loop. 
        else:						# Else if not all the conditions were met... 
            print ("Your password needs a lower case letter, an upper case letter, a number, and either $, #, or @.")	# Prints error message. 
if PasswordCheck == 2:                                  # If the user completed the process... 
    print ("Welcome " + Username)                       # Welcomes the user. 
