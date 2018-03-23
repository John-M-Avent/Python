
import random

print("\n ____________________________________")
print(" Welcome to the program. ")
print(" At any point, type 'exit' to exit. ")
print(" ____________________________________")

Guessing_Game_Scoreboard = ["Bot"]
Guessing_Game_Scores = {"Bot" : 100000000000}

Loop_Control_Variable = 1

while Loop_Control_Variable == 1:
    print("\n ____________________________________")
    print(" Below are the numbered menu options.")
    print(" 1)   :   Instructions")
    print(" 2)   :   Number Guessing Game")
    print(" 3)   :   Roll Some Dice")
    print(" 4)   :   ")
    print(" 5)   :   ")
    print(" 6)   :   ")
    print(" 7)   :   ")
    print(" 8)   :   ")
    print(" 9)   :   ")
    print(" 0)   :   Exit")
    print(" ____________________________________")
    Menu_Input = input(" Enter a number to select an option: ")
    if Menu_Input == "exit":
        print(" Thank you for running this program.")
        print(" ____________________________________\n")
        break
    elif Menu_Input == "1":
        print("\n Enter a number to select an option of off the menu.")
        print(" At any point, type 'exit' to exit the whole program.")
    elif Menu_Input == "2":
        
        print("\n ____________________________________")
        print(" Welcome to the Number Guessing Game. ")
        print(" You must guess a random number.")
        print(" ____________________________________")

        Intro_Input_Loop_Control_Variable = 1

        while Intro_Input_Loop_Control_Variable == 1:
            print("\n ____________________________________")
            print(" Below are the numbered menu options.")
            print(" 1)   :   Game Instructions")
            print(" 2)   :   Start New Game")
            print(" 3)   :   Scoreboard")
            print(" 0)   :   Quit Game")
            print(" ____________________________________")
            Game_Menu_Input = input(" Enter a number to select an option: ")
            if Game_Menu_Input == "exit":
                print(" Thank's for playing! ")
                print(" ____________________________________\n")
                Loop_Control_Variable = 0
                break
            elif Game_Menu_Input == "1":
                print("\n The objective of the game is to guess a \n andomly generated number between 1 and 10,000.")
                print(" The game tells you if your guess it too high\n or too low.  Good luck!")
            elif Game_Menu_Input == "2":
                Random_Number = random.randint(1,100)
                Run_Game_Loop_Control_Variable = 1
                Score = 0
                print("")
                while Run_Game_Loop_Control_Variable == 1:
                    User_Guess = input(" Enter an integer (or 'quit'): ")
                    if User_Guess == "exit":
                        print(" Thank's for playing! ")
                        print(" ____________________________________\n")
                        Loop_Control_Variable = 0
                        Intro_Input_Loop_Control_Variable = 0
                        break
                    elif User_Guess == "quit":
                        print(" Thank's for playing! ")
                        print(" ____________________________________\n")
                        break
                    else:
                        User_Guess_Int = int(User_Guess)
                        if User_Guess_Int == Random_Number:
                            Run_Game_Loop_Control_Variable = 0
                            print(" Congrats, you guessed correctly!")
                            print(" Your score is: " + str(Score) )
                            Player_Name = input(" Enter a name to save your score. ")
                            Guessing_Game_Scores[Player_Name] = Score
                            Position = 0
                            for i in Guessing_Game_Scores:
                                if Score > Guessing_Game_Scores[i]:
                                    Position += 1
                            Guessing_Game_Scoreboard.insert(Position,Player_Name)
                        elif User_Guess_Int > Random_Number:
                            print(" Your guess is too high.")
                            Score += 1
                        elif User_Guess_Int < Random_Number:
                            print(" Your guess is too low.")
                            Score += 1

            elif Game_Menu_Input == "3":
                print(" Scoreboard: ")
                Number_of_Scores = len(Guessing_Game_Scoreboard) - 1
                for Current_Position in range(0, Number_of_Scores):
                    print(" #" + str(Current_Position + 1) + ": " + Guessing_Game_Scoreboard[Current_Position]
                          + "   : " + str(Guessing_Game_Scores[Guessing_Game_Scoreboard[Current_Position]]))
            elif Game_Menu_Input == "0":
                print(" Thank's for playing! ")
                print(" ____________________________________\n")
                break
            else:
                print("\n Please enter an option listed on the menu.")
                
    elif Menu_Input == "3":
        print("\n ____________________________________")
        print(" Here you can simulater rolling dice.")
        Number_of_Dice = input(" Enter the number of dice to roll: ")
        if Number_of_Dice == 'exit':
            print("\n Thank's for playing! ")
            print(" ____________________________________\n")
            Loop_Control_Variable = 0
            break
        else:
            Number_of_Dice = int(Number_of_Dice)
            Roll = random.randint(Number_of_Dice, Number_of_Dice*6)
            print("\n The result is " + str(Roll) + " for " + str(Number_of_Dice) + " dice rolled.")
    elif Menu_Input == "4":
        a = 1
    elif Menu_Input == "5":
        a = 1
    elif Menu_Input == "6":
        a = 1
    elif Menu_Input == "7":
        a = 1
    elif Menu_Input == "8":
        a = 1
    elif Menu_Input == "9":
        a = 1
    elif Menu_Input == "0":
        print("\n Thank you for running this program.")
        print(" ____________________________________\n")
        break
    else:
        print(" Please enter an option listed on the menu.")
