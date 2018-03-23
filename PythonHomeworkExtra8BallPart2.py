## Python Homework Extra: 8-Ball Part 2
# John M. Avent 
# ENG 101-06 
# 5/1/2017 
# 
# Setup
# 
import random                                                                       # Imports the random functions. 
ResponseListPositive = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definetly.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes."]
# List of positives responses. 
ResponseListNeutral = ["Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again."]
# List of neutral responses. 
ResponseListNegative = ["Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."] 
# List of negative responses. 
ResponseList = ResponseListPositive + ResponseListNeutral + ResponseListNegative    # Adds the response lists together. 
ResponseNumbered = {}                                                               # Blank dictionary. 
ResponseCount = {}                                                                  # Blank dictionary. 
#
# Building Dictionaries 
# 
Number = 0                                                                          # Makes a number to number the responses. 
for Item in ResponseList:                                                           # For reseponse in the list of responses... 
    Number += 1                                                                     # Adds one to the number. 
    ResponseNumbered[Number] = Item                                                 # In the numbered dictionary of responses, the key is the number and the value is the response. 
    ResponseCount[Item] = 0                                                         # In the count dictionary the key is the response and the value is the count, starting at 0.
# This method of building dictionaries allows me to add or remove as many responses as need be. 
#
# Questions and Answers 
# 
Question = 1                                                                        # Makes a variable to run the 'while' loop off of. 
while Question != 'done':                                                           # Runs a 'while' loop while the variable is not 'done'. 
    Question = input ("Enter your question or type 'done' when finished: ")         # Queries the user for their question. 
    QuestionLower = Question.lower()                                                # Makes the question lowercase. 
    if QuestionLower == 'done':                                                     # If the user types "done"... 
        break                                                                       # Breaks the 'while' loop. 
    else:                                                                           # Else...
        KeepRunning = 100                                                           # Makes the loop variable 100. 
        while KeepRunning > 0:                                                      # While the loop variable is greater than 0... 
            ResponseNumber = random.randint(1,Number)                               # Generates a random number from 1 to the number of responses there are. 
            Response = ResponseNumbered[ResponseNumber]                             # Puts the random number into the dictionary as a key to get a response out. 
            print (Response)                                                        # Prints the response. 
            ResponseCount[Response] += 1                                            # Adds one to the number of times that response has been used. 
            KeepRunning -= 1                                                        # Subtracts 1 from the loop variable. 
