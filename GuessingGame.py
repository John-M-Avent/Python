# John M. Avent
# Python Seminar Code
# Created 3-23-2018
#
# This is a number guessing game. The game will generate a number and the
# user must guess it. There is a scoreboard for the best scores.
#
# These are headers and need to be placed at the start of any code this is copied into
Guessing_Game_Scoreboard = ["Bot"]              # Initializes Sorted Scoreboard
Guessing_Game_Scores = {"Bot" : 100000000000}   # Initializes Unsorted Score Dictionary
import random
#
# Setup
#
# Prints header for the Number Guessing Game
print("\n ____________________________________")
print(" Welcome to the Number Guessing Game. ")
print(" You must guess a random number.")
print(" ____________________________________")

#
# The Game Loop
#
Intro_Input_Loop_Control_Variable = 1           # Initializes the loop control variable

while Intro_Input_Loop_Control_Variable == 1:
    # Game Menu Header
    print("\n ____________________________________")
    print(" Below are the numbered menu options.")
    print(" 1)   :   Game Instructions")
    print(" 2)   :   Start New Game")
    print(" 3)   :   Scoreboard")
    print(" 0)   :   Quit Game")
    print(" ____________________________________")
    # Option Selection
    Game_Menu_Input = input(" Enter a number to select an option: ")
    #
    # Selection Evaluation
    #
    if Game_Menu_Input == "exit":               # The exits the main program as well
        print(" Thank's for playing! ")
        print(" ____________________________________\n")
        Loop_Control_Variable = 0
        break
    #
    elif Game_Menu_Input == "1":                # The game's instructions
        print("\n The objective of the game is to guess a \n andomly generated number between 1 and 10,000.")
        print(" The game tells you if your guess it too high\n or too low.  Good luck!")
    #
    elif Game_Menu_Input == "2":                # Time to play
        Random_Number = random.randint(1,10000)   # Generates the random number to be guessed
        Run_Game_Loop_Control_Variable = 1      # Here is the loop control variable for the game
        Score = 0                               # Initialize score to 0
        print("")
        while Run_Game_Loop_Control_Variable == 1:  # The body of the game
            User_Guess = input(" Enter an integer (or 'quit'): ")   # User guesses
            #
            if User_Guess == "exit":            # Exits the whole Program
                # Prints exit message
                print(" Thank's for playing! ")
                print(" ____________________________________\n")
                Loop_Control_Variable = 0
                Intro_Input_Loop_Control_Variable = 0
                break
            #
            elif User_Guess == "quit":           # Exits just the guessing stage
                print(" Thank's for playing! ")
                print(" ____________________________________\n")
                break
            #
            else:
                User_Guess_Int = int(User_Guess)                    # Converts guess to int
                if User_Guess_Int == Random_Number:                 # If the guess was correct
                    Run_Game_Loop_Control_Variable = 0              # The game ends when the loop finishes
                    print(" Congrats, you guessed correctly!")
                    print(" Your score is: " + str(Score) )
                    #
                    # Below this is scoreboard stuff
                    #
                    Player_Name = input(" Enter a name to save your score. ")   # Takes player name
                    Guessing_Game_Scores[Player_Name] = Score   # Adds name and score into unsorted score dictionary
                    Position = 0
                    # This loop finds the position where the score is less than or equal to the current players score
                    for i in Guessing_Game_Scores:
                        if Score > Guessing_Game_Scores[i]:
                            Position += 1
                    # This inserts the user's name in the correct spot on the sorted scoreboard list
                    Guessing_Game_Scoreboard.insert(Position,Player_Name)
                #
                elif User_Guess_Int > Random_Number:                # The user guessed too high
                    print(" Your guess is too high.")
                    Score += 1
                #
                elif User_Guess_Int < Random_Number:                # The user guessed too low
                    print(" Your guess is too low.")
                    Score += 1
    #
    elif Game_Menu_Input == "3":                # Display the scoreobard
        print(" Scoreboard: ")
        # This takes the number of scores on the scoreboard - 1
        Number_of_Scores = len(Guessing_Game_Scoreboard) - 1
        # This runs through every element in the scoreboard
        for Current_Position in range(0, Number_of_Scores):
            # This prints the place the player is in, the scoreboard referenced at that place,
            # and the score dictionary referenced at the player name from that place
            print(" #" + str(Current_Position + 1) + ": " + Guessing_Game_Scoreboard[Current_Position]
                  + "   : " + str(Guessing_Game_Scores[Guessing_Game_Scoreboard[Current_Position]]))
    #
    elif Game_Menu_Input == "0":
        # Prints quit message
        print(" Thank's for playing! ")
        print(" ____________________________________\n")
        break
    #
    else:                   # If the user entered something not on the list
        print("\n Please enter an option listed on the menu.")
