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
        a = 1
    elif Game_Menu_Input == "2":
        Random_Number = random.randint(1,10000)
        Run_Game_Loop_Control_Variable = 1
        Score = 0
        print("")
        while Run_Game_Loop_Control_Variable == 1:
            User_Guess = input(" Enter an integer (or 'quit'): ")
            if User_Guess == "exit":
                print(" Thank's for playing! ")
                print(" ____________________________________\n")
                Loop_Control_Variable = 0
                break
            elif User_Guess == "exit":
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
                    Temp_Name = Player_Name
                    Position = 0
                    for i in Guessing_Game_Scoreboard:
                        if Guessing_Game_Scores[Temp_Name] >= Guessing_Game_Scores[i]:
                            Guessing_Game_Scoreboard[Position] = Temp_Name
                            Temp_Name = i
                        Position += 1
                elif User_Guess_Int > Random_Number:
                    print(" Your guess is too high.")
                    Score += 1
                elif User_Guess_Int < Random_Number:
                    print(" Your guess is too low.")
                    Score += 1

    elif Game_Menu_Input == "3":
        print(" Scoreboard: ")
        for Position in range[0, len(Guessing_Game_Scoreboard)]:
            print(" #" + str(Position + 1) + ": " + Guessing_Game_Scores[Position] + "   : " + Guessing_Game_Scores[Guessing_Game_Scores[Position]])
    elif Game_Menu_Input == "0":
        print(" Thank's for playing! ")
        print(" ____________________________________\n")
        break
    else:
        print(" Please enter an option listed on the menu.")
