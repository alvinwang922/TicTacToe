import random #Imports library to use random integer generator function
import os #Imports library to use clear screen function
import time #Imports library to use program delay function


#VARIABLES TO BE USED THROUGHOUT THE PROJECT

start_game = True #To determine whether or not to start the game again
welcome = "Welcome to a game of Tic-Tac-Toe by Alvin Wang.\n"\
"Tic Tac Toe Board\n"\
"     |     |     \n"\
"  1  |  2  |  3  \n"\
"_____|_____|_____\n"\
"     |     |     \n"\
"  4  |  5  |  6  \n"\
"_____|_____|_____\n"\
"     |     |     \n"\
"  7  |  8  |  9  \n"\
"     |     |     \n"\
"To exit, press ctrl + c and, if prompted, type in quit().\n"\
"To make a move, type in the number (1-9) that corresponds to the space you want to fill with your symbol.\n"\
"Whoever gets 3 of their symbols in a row wins. Good Luck and have fun!\n"\
"____________GAME MODES___________\n"\
"|------------Player X|Player 0--|     (Player X goes first)\n"\
"|____________________|__________|\n"\
"|Input A for Human   |Human     |\n"\
"|Input B for Human   |RandomAI  |\n"\
"|Input C for RandomAI|Human     |\n"\
"|Input D for Human   |SmartAI   |\n"\
"|Input E for SmartAI |Human     |\n"\
"|Input F for RandomAI|RandomAI  |\n"\
"|Input G for SmartAI |RandomAI  |\n"\
"|Input H for RandomAI|SmartAI   |\n"\
"|Input I for SmartAI |SmartAI   |\n"\
"|____________________|__________|"#Welcome message, instructions, and game modes
space_1 = " " #Just representations of spaces on the board
space_2 = " " #The two representing game pieces are 0 and X
space_3 = " "
space_4 = " "
space_5 = " "
space_6 = " "
space_7 = " "
space_8 = " "
space_9 = " "
winner = "No one..." #Determines who the winner is
game_over = False #Determines whether the game is over or not
turn = "X" #Represents which player ("X" or "0") is going next ("X" should always start)
invalid_move = False #Should be True when an invalid move is made
game_mode = "Unknown..." #Determines which game mode is to be initated



#FUNCTIONS TO BE USED DURING ACTUAL GAMEPLAY

def Start(): #Prints start-of-game message
    print(welcome)

def Board(): #Prints game board
    global space_1, space_2, space_3, space_4, space_5, space_6, space_7, space_8, space_9 #Allows variables to be redefined globally
    if game_over is False: #Checks to see if the game ended yet
        if space_1 == " ": #Checks to see if the space is blank
            space_1 = "1" #Replaces the space with a number for player's reference
        if space_2 == " ": #Checks to see if the space is blank
           space_2 = "2" #Replaces the space with a number for player's reference
        if space_3 == " ": #Checks to see if the space is blank
           space_3 = "3" #Replaces the space with a number for player's reference
        if space_4 == " ": #Checks to see if the space is blank
           space_4 = "4" #Replaces the space with a number for player's reference
        if space_5 == " ": #Checks to see if the space is blank
           space_5 = "5" #Replaces the space with a number for player's reference
        if space_6 == " ": #Checks to see if the space is blank
           space_6 = "6" #Replaces the space with a number for player's reference
        if space_7 == " ": #Checks to see if the space is blank
           space_7 = "7" #Replaces the space with a number for player's reference
        if space_8 == " ": #Checks to see if the space is blank
           space_8 = "8" #Replaces the space with a number for player's reference
        if space_9 == " ": #Checks to see if the space is blank
           space_9 = "9" #Replaces the space with a number for player's reference
    print("Tic Tac Toe Board") #Title of board
    print("     |     |     ")
    print("  "+space_1+"  |  "+space_2+"  |  "+space_3+"  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  "+space_4+"  |  "+space_5+"  |  "+space_6+" ")
    print("_____|_____|_____")
    print("     |     |")
    print("  "+space_7+"  |  "+space_8+"  |  "+space_9+" ")
    print("     |     |     ")
    if space_1 == "1": #Checks to see if the space was replaced by a number
        space_1 = " " #Replaces any numbered spaces with blank spaces
    if space_2 == "2": #Checks to see if the space was replaced by a number
       space_2 = " " #Replaces any numbered spaces with blank spaces
    if space_3 == "3": #Checks to see if the space was replaced by a number
       space_3 = " " #Replaces any numbered spaces with blank spaces
    if space_4 == "4": #Checks to see if the space was replaced by a number
       space_4 = " " #Replaces any numbered spaces with blank spaces
    if space_5 == "5": #Checks to see if the space was replaced by a number
       space_5 = " " #Replaces any numbered spaces with blank spaces
    if space_6 == "6": #Checks to see if the space was replaced by a number
       space_6 = " " #Replaces any numbered spaces with blank spaces
    if space_7 == "7": #Checks to see if the space was replaced by a number
       space_7 = " " #Replaces any numbered spaces with blank spaces
    if space_8 == "8": #Checks to see if the space was replaced by a number
       space_8 = " " #Replaces any numbered spaces with blank spaces
    if space_9 == "9": #Checks to see if the space was replaced by a number
       space_9 = " " #Replaces any numbered spaces with blank spaces
    print("                        Tic Tac Toe Board") #Title of board
    print("                             |     |     ")
    print("                          "+space_1+"  |  "+space_2+"  |  "+space_3+"  ")
    print("                        _____|_____|_____")
    print("                             |     |     ")
    print("                          "+space_4+"  |  "+space_5+"  |  "+space_6+" ")
    print("                        _____|_____|_____")
    print("                             |     |")
    print("                          "+space_7+"  |  "+space_8+"  |  "+space_9+" ")
    print("                             |     |     ")
    #Above lines form an ASCII art board
    
def Win(): #Determines whether the board is a winning board
    global game_over, winner
    if space_1 == space_2 == space_3 == "0" or space_4 == space_5 == space_6 == "0" or space_7 == space_8 == space_9 == "0" or space_1 == space_5 == space_9 == "0" or\
    space_1 == space_4 == space_7 == "0" or space_2 == space_5 == space_8 == "0" or space_3 == space_6 == space_9 == "0" or space_3 == space_5 == space_7 == "0":
    #Checks for all possible winning situations for player "0"
        game_over = True #Tells that the game is over
        winner = "0" #Determines who is the winner by redefining that variable
        return True #Informs that the board is in a state that wins the game
    elif space_1 == space_2 == space_3 == "X" or space_4 == space_5 == space_6 == "X" or space_7 == space_8 == space_9 == "X" or space_1 == space_5 == space_9 == "X" or\
    space_1 == space_4 == space_7 == "X" or space_2 == space_5 == space_8 == "X" or space_3 == space_6 == space_9 == "X" or space_3 == space_5 == space_7 == "X":
    #Checks for all possible winning situations for player "X"
        game_over = True #Tells that the game is over
        winner = "X" #Determines who is the winner by redefining that variable
        return True #Informs that the board is in a state that wins the game
    elif space_1 is not " " and space_2 is not " " and space_3 is not " " and space_4 is not " " and space_5 is not " " and space_6 is not " " and space_7 is not " " and space_8 is not " " and space_9 is not " ":
    #Checks for a "cat's game" where there is no winner 
        game_over = True #Tells that the game is over
    else: #Tells us that the board did not pass the win conditions
        return False #Informs that the current board does not result in a win

def MakeMove(player, space): #Used to make a move as well as determine if the move is valid (usage example: MakeMove("X",1) and parameters are MakeMove("X"/"0",1-9))
    global space_1, space_2, space_3, space_4, space_5, space_6, space_7, space_8, space_9, invalid_move #Used to allow these variables to be redefined globally rather than just in this function
    if space == "1": #Used to determine which space to edit
        if space_1 == " ": #Used to determine whether the space that was selected is empty
            space_1 = player #Used to replace the empty space on the board with the player's symbol
            invalid_move = False #Tells that the move is not invalid by altering the invalid_move variable and letting us know that the move was invalid
            return True #Returning True so that you know the move you made was viable and the space you selected will be replaced
        else: #Leading the computer to making the decision to return False in the next line because the space selected had something other than a single space inside
            invalid_move = True #Allowing the player to choose another space to place their piece by altering the invalid_move variable and letting us know that the move was invalid
            print("Space already filled. Please try again.") #Returning "Invalid move." so that you know the move you made was rejected
            return False #Returns False so that you know that the move was not viable and nothing was done
    elif space == "2": #Used to determine which space to edit
        if space_2 == " ": #Used to determine whether the space that was selected is empty
            space_2 = player #Used to replace the empty space on the board with the player's symbol
            invalid_move = False #Tells that the move is not invalid by altering the invalid_move variable and letting us know that the move was invalid
            return True #Returning True so that you know the move you made was viable and the space you selected will be replaced
        else: #Leading the computer to making the decision to return False in the next line because the space selected had something other than a single space inside
            invalid_move = True #Allowing the player to choose another space to place their piece by altering the invalid_move variable and letting us know that the move was invalid
            print("Space already filled. Please try again.") #Returning "Invalid move." so that you know the move you made was rejected
            return False #Returns False so that you know that the move was not viable and nothing was done
    elif space == "3": #Used to determine which space to edit
        if space_3 == " ": #Used to determine whether the space that was selected is empty
            space_3 = player #Used to replace the empty space on the board with the player's symbol
            invalid_move = False #Tells that the move is not invalid by altering the invalid_move variable and letting us know that the move was invalid
            return True #Returning True so that you know the move you made was viable and the space you selected will be replaced
        else: #Leading the computer to making the decision to return False in the next line because the space selected had something other than a single space inside
            invalid_move = True #Allowing the player to choose another space to place their piece by altering the invalid_move variable and letting us know that the move was invalid
            print("Space already filled. Please try again.") #Returning "Invalid move." so that you know the move you made was rejected
            return False #Returns False so that you know that the move was not viable and nothing was done
    elif space == "4": #Used to determine which space to edit
        if space_4 == " ": #Used to determine whether the space that was selected is empty
            space_4 = player #Used to replace the empty space on the board with the player's symbol
            invalid_move = False #Tells that the move is not invalid by altering the invalid_move variable and letting us know that the move was invalid
            return True #Returning True so that you know the move you made was viable and the space you selected will be replaced
        else: #Leading the computer to making the decision to return False in the next line because the space selected had something other than a single space inside
            invalid_move = True #Allowing the player to choose another space to place their piece by altering the invalid_move variable and letting us know that the move was invalid
            print("Space already filled. Please try again.") #Returning "Invalid move." so that you know the move you made was rejected
            return False #Returns False so that you know that the move was not viable and nothing was done
    elif space == "5": #Used to determine which space to edit
        if space_5 == " ": #Used to determine whether the space that was selected is empty
            space_5 = player #Used to replace the empty space on the board with the player's symbol
            invalid_move = False #Tells that the move is not invalid by altering the invalid_move variable and letting us know that the move was invalid
            return True #Returning True so that you know the move you made was viable and the space you selected will be replaced
        else: #Leading the computer to making the decision to return False in the next line because the space selected had something other than a single space inside
            invalid_move = True #Allowing the player to choose another space to place their piece by altering the invalid_move variable and letting us know that the move was invalid
            print("Space already filled. Please try again.") #Returning "Invalid move." so that you know the move you made was rejected
            return False #Returns False so that you know that the move was not viable and nothing was done
    elif space == "6": #Used to determine which space to edit
        if space_6 == " ": #Used to determine whether the space that was selected is empty
            space_6 = player #Used to replace the empty space on the board with the player's symbol
            invalid_move = False #Tells that the move is not invalid by altering the invalid_move variable and letting us know that the move was invalid
            return True #Returning True so that you know the move you made was viable and the space you selected will be replaced
        else: #Leading the computer to making the decision to return False in the next line because the space selected had something other than a single space inside
            invalid_move = True #Allowing the player to choose another space to place their piece by altering the invalid_move variable and letting us know that the move was invalid
            print("Space already filled. Please try again.") #Returning "Invalid move." so that you know the move you made was rejected
            return False #Returns False so that you know that the move was not viable and nothing was done
    elif space == "7": #Used to determine which space to edit
        if space_7 == " ": #Used to determine whether the space that was selected is empty
            space_7 = player #Used to replace the empty space on the board with the player's symbol
            invalid_move = False #Tells that the move is not invalid by altering the invalid_move variable and letting us know that the move was invalid
            return True #Returning True so that you know the move you made was viable and the space you selected will be replaced
        else: #Leading the computer to making the decision to return False in the next line because the space selected had something other than a single space inside
            invalid_move = True #Allowing the player to choose another space to place their piece by altering the invalid_move variable and letting us know that the move was invalid
            print("Space already filled. Please try again.") #Returning "Invalid move." so that you know the move you made was rejected
            return False #Returns False so that you know that the move was not viable and nothing was done
    elif space == "8": #Used to determine which space to edit
        if space_8 == " ": #Used to determine whether the space that was selected is empty
            space_8 = player #Used to replace the empty space on the board with the player's symbol
            invalid_move = False #Tells that the move is not invalid by altering the invalid_move variable and letting us know that the move was invalid
            return True #Returning True so that you know the move you made was viable and the space you selected will be replaced
        else: #Leading the computer to making the decision to return False in the next line because the space selected had something other than a single space inside
            invalid_move = True #Allowing the player to choose another space to place their piece by altering the invalid_move variable and letting us know that the move was invalid
            print("Space already filled. Please try again.") #Returning "Invalid move." so that you know the move you made was rejected
            return False #Returns False so that you know that the move was not viable and nothing was done
    elif space == "9": #Used to determine which space to edit
        if space_9 == " ": #Used to determine whether the space that was selected is empty
            space_9 = player #Used to replace the empty space on the board with the player's symbol
            invalid_move = False #Tells that the move is not invalid by altering the invalid_move variable and letting us know that the move was invalid
            return True #Returning True so that you know the move you made was viable and the space you selected will be replaced
        else: #Leading the computer to making the decision to return False in the next line because the space selected had something other than a single space inside
            invalid_move = True #Allowing the player to choose another space to place their piece by altering the invalid_move variable and letting us know that the move was invalid
            print("Space already filled. Please try again.") #Returning "Invalid move." so that you know the move you made was rejected
            return False #Returns False so that you know that the move was not viable and nothing was done
    else: #Checks for if the input was something random other than 1-9
        os.system('cls') #Clears screen
        Board() #Prints out the current board to remind the player of the board's current status
        print("Please type a number from 1-9.") #Informs the player that their input was not valid and they should enter a number from 1-9
        invalid_move = True #Tells that the move is invalid by altering the invalid_move variable and letting us know that the move was invalid
        return False #Returning False so that you know the move was not viable and nothing was done

def HumanInput(): #Game mode function for humans who actually are playing this on a computer
    return input("Type the location number and press enter to place your piece:") #Asks the player to input their move

def RandomAI(): #An artificial intelligence that randomly fill in any random space on the board
    return str(random.randint(1,9)) #Generates a random number to represent the spot where the RandomAI will place its piece

def SmartAI(): #An artificial intelligence that properly plays the game of TicTacToe (meaning that it is "unbeatable") by taking priority in taking the middle spot and then checking for winning oppurtunities, then for losing oppurtunities.
#Then, it finally checks for corner spots and only puts a corner spot if the opponent does not have 2 corners already, ending by checking for edge spots.
    win_1 = [space_1, space_2, space_3, "1", "2", "3"]
    win_2 = [space_4, space_5, space_6, "4", "5", "6"]
    win_3 = [space_7, space_8, space_9, "7", "8", "9"]
    win_4 = [space_1, space_4, space_7, "1", "4", "7"]
    win_5 = [space_2, space_5, space_8, "2", "5", "8"]
    win_6 = [space_3, space_6, space_9, "3", "6", "9"]
    win_7 = [space_1, space_5, space_9, "1", "5", "9"]
    win_8 = [space_3, space_5, space_7, "3", "5", "7"]
    wins = [win_1, win_2, win_3, win_4, win_5, win_6, win_7, win_8]
    move = " "
    if space_5 is " ": #Checks if the center spot is empty
        move = "5" #Takes the middle square
    else:
        for move_a in wins: #For loop to check if the board is in a winning state for the SmartAI
            if move_a[0] == move_a[1] == turn and move_a[2] == " ": #Checking first combination of spaces for winning state
                move = move_a[5] #Making move if the combination is found
            elif move_a[0] == move_a[2] == turn and move_a[1] == " ": #Checking second combination of spaces for winning state
                move = move_a[4] #Making move if the combination is found
            elif move_a[1] == move_a[2] == turn and move_a[0] == " ": #
                move = move_a[3] #Making move if the combination is found
        if move == " ": #Checks if a space has been selected for a move
            for move_b in wins: #For loop to check if the board is in a winning state for the opponent
                if move_b[0] == move_b[1] != " " and move_b[2] == " ": #Checking first combination of spaces for winning state
                    move = move_b[5] #Making move if the combination is found
                elif move_b[0] == move_b[2] != " " and move_b[1] == " ": #Checking first combination of spaces for winning state
                    move = move_b[4] #Making move if the combination is found
                elif move_b[1] == move_b[2] != " " and move_b[0] == " ":
                    move = move_b[3] #Making move if the combination is found
            if move == " ": #Checks if a space has been selected for a move
                if space_1 == space_3 != " " and space_1 == space_3 != turn or space_3 == space_7 != " " and space_3 == space_7 != turn or space_7 == space_9 != " " and space_7 == space_9 != turn or space_1 == space_7 != " "\
                and space_1 == space_7 != turn or space_1 == space_9 != " " and space_1 == space_9 != turn or space_3 == space_9 != " " and space_3 == space_9 != turn:
                #Checks if the other player is doing a particular trick when they go first (by taking three corners and forcing out a win)
                    if space_2 is " ": #Checks if the edge spots are available
                        move = "2" #Makes the move to take the edge spot
                    elif space_4 is " ": #Checks if the edge spots are available
                        move = "4" #Makes the move to take the edge spot
                    elif space_6 is " ": #Checks if the edge spots are available
                        move = "6" #Makes the move to take the edge spot
                    elif space_8 is " ": #Checks if the edge spots are available
                        move = "8" #Makes the move to take the edge spot
                elif space_1 == " " or space_3 == " " or space_7 == " " or space_9 == " ":
                    SmartAI_random_variable = random.randint(1,4) #Generates a random number to determine which space to fill
                    if SmartAI_random_variable is 1: #Checks if the corner spot is open since corner spots are more advantageous
                        move = "1" #Makes the move to take the corner spot
                    elif SmartAI_random_variable is 2: #Checks if the corner spot is open since corner spots are more advantageous
                        move = "3" #Makes the move to take the corner spoter spot
                    elif SmartAI_random_variable is 3: #Checks if the corner spot is open since corner spots are more advantageous
                        move = "7" #Makes the move to take the corn= " "or space_9 == " ": #Checks if corner spots are open
                    elif SmartAI_random_variable is 4: #Checks if the corner spot is open since corner spots are more advantageous
                        move = "9" #Makes the move to take the corner spot
                elif space_2 == " " or space_4 == " " or space_6 == " " or space_8 == " ": #Checks if edge spots are open
                    SmartAI_random_variable = random.randint(1,4) #Generates a random number to determine which space to fill
                    if SmartAI_random_variable is 1: #Checks if the edge spots are available
                        move = "2" #Makes the move to take the edge spot
                    elif SmartAI_random_variable is 2: #Checks if the edge spots are available
                        move = "4" #Makes the move to take the edge spot
                    elif SmartAI_random_variable is 3: #Checks if the edge spots are available
                        move = "6" #Makes the move to take the edge spot
                    elif SmartAI_random_variable is 4: #Checks if the edge spots are available
                        move = "8" #Makes the move to take the edge spot
    return move #Makes the optimal move for the SmartAI


#WHILE LOOPS FORMING STRUCTURE OF THE ACTUAL GAMEPLAY

while start_game is True: #Allows the game to be restarted if the player chooses to do so and also allows the player to be continuously bothered if they do not input "Y" or "N" for if they want to play again
    if game_over is False: #So that the player does not see the start message every time they input something other than "Y" or "N" for if they want to play again
        if game_mode is "Unknown...": #Checks to see if the game mode has not been determined yet
            Start() #Start messsage and instructions are printed
            restart_game = "?" #Allows the winner to be seen in case the player reset the game
        game_mode = input("Please type the letter of your game mode and press enter:")
        if game_mode is "A" or game_mode is "a": #Checks to see if the player selected Game Mode A
            player_one_strategy = HumanInput #Defines that a human will play as player 1
            player_two_strategy = HumanInput #Defines that a human will play as player 2
        elif game_mode is "B" or game_mode is "b": #Checks to see if the player selected Game Mode B
            player_one_strategy = HumanInput #Defines that a human will play as player 1
            player_two_strategy = RandomAI #Defines that the RandomAI will play as player 2
        elif game_mode is "C" or game_mode is "c": #Checks to see if the player selected Game Mode C
            player_one_strategy = RandomAI #Defines that the RandomAI will play as player 1
            player_two_strategy = HumanInput #Defines that a human will play as player 2
        elif game_mode is "D" or game_mode is "d": #Checks to see if the player selected Game Mode D
            player_one_strategy = HumanInput #Defines that a human will play as player 1
            player_two_strategy = SmartAI #Defines that the SmartAI will play as player 2
        elif game_mode is "E" or game_mode is "e": #Checks to see if the player selected Game Mode E
            player_one_strategy = SmartAI #Defines that the SmartAI will play as player 1
            player_two_strategy = HumanInput #Defines that a human will play as player 2
        elif game_mode is "F" or game_mode is "f": #Checks to see if the player selected Game Mode F
            player_one_strategy = RandomAI #Defines that the RandomAI will play as player 1
            player_two_strategy = RandomAI #Defines that the RandomAI will play as player 2
        elif game_mode is "G" or game_mode is "g": #Checks to see if the player selected Game Mode G
            player_one_strategy = SmartAI #Defines that the SmartAI will play as player 1
            player_two_strategy = RandomAI #Defines that the RandomAI will play as player 2
        elif game_mode is "H" or game_mode is "h": #Checks to see if the player selected Game Mode H
            player_one_strategy = RandomAI #Defines that the RandomAI will play as player 1
            player_two_strategy = SmartAI #Defines that the SmartAI will play as player 2
        elif game_mode is "I" or game_mode is "i": #Checks to see if the player selected Game Mode I
            player_one_strategy = SmartAI #Defines that the SmartAI will play as player 1
            player_two_strategy = SmartAI #Defines that the SmartAI will play as player 2
        else: #Leads the computer to do what follows only if a game mode was not selected
            print("Invalid game mode. Please type in A, B, C, D, E, F, G, H, or I.") #Skips the rest of this while loop and restarts so that the player can input a viable space
        while game_over is False and game_mode is "A" or game_over is False and game_mode is "B" or game_over is False and game_mode is "C" or game_over is False and game_mode is "D" or game_over is False and game_mode is "E" or\
        game_over is False and game_mode is "F" or game_over is False and game_mode is "G" or game_over is False and game_mode is "H" or game_over is False and game_mode is "I" or\
        game_over is False and game_mode is "a" or game_over is False and game_mode is "b" or game_over is False and game_mode is "c" or game_over is False and game_mode is "d" or game_over is False and game_mode is "e" or\
        game_over is False and game_mode is "f" or game_over is False and game_mode is "g" or game_over is False and game_mode is "h" or game_over is False and game_mode is "i":
        #Forms a loop so that each turn can be repeated without a need to rewrite all the code
            if invalid_move is False: #So that you do not see an unnecessary repeated board and will just see the error message when you make an invalid move
                #os.system('cls') #Clears screen
                Board() #Prints out board for players to see what is going on
            print("It is Player " + turn + "'s turn.") #Tells the players who's turn it is
            if turn is "X": #Checks if it is player "X"'s turn
                strategy = player_one_strategy() #Recalls the function that represents player "X"'s turn
            elif turn is "0": #Checks if it is player "0"'s turn
                strategy = player_two_strategy() #Recalls the funciton that represents player "0"'s turn
            MakeMove(turn, strategy) #Recalls the function that makes a move for the current player and checks for move validity
            if invalid_move is False: #Checks for if an invalid move occured on this turn
                if turn is "X": #Checks for if it is player "X"'s turn
                    turn = "0" #Switches the turn to player "0"'s turn
                elif turn is "0": #Checks for if it is player "0"'s turn
                    turn = "X" #Switches the turn to player "X"'s turn
            Win() #Checks for if the board is in a winning state
    if game_over is True and restart_game is "?": #Checks to see if there was an input for restart_game so that the winner is not restated multiple times and the players can see the error message that they need to input either "Y" or "N"
        os.system('cls') #Clears screen
        if winner is "No one...": #Checks to see if there was no winner
            print("Game over! No player won...it was a cat's game! MMMEEEOOOWWW!!!") #Tells the players that no one one and it was a "cat's game"
            Board() #Prints out final board so players can see what happened in the end
        elif winner is not "No one...": #Checks to see if someone actually won
            print("Game over! Player " + winner + " won!!!") #Tells the players who won
            Board() #Prints out final board so players can see what happened in the end
    if game_over is True: #Checks if the game is really over and it is not just a repeat due to an improper way of selecting a game mode
        restart_game = input("Wanna play again? Type Y or N and then press enter:") #Asks the players if they want to play again
        if restart_game == "Y" or restart_game == "y": #Checks to see if the players wanted to restart the game
            space_1 = space_2 = space_3 = space_4 = space_5 = space_6 = space_7 = space_8 = space_9 = " " #Resets all the spaces on the board
            game_over, winner, game_mode, turn = False, "No one...", "Unknown...", "X" #Resets the variables so that the game can restart
            os.system('cls') #Clears screen
        elif restart_game == "N" or restart_game == "n": #Checks to see if the players wanted to stop playing
            start_game = False #Changes the start_game variable so that the while loop will stop
            print("See ya!") #Goodbye message
            time.sleep(2) #Delays the program from exiting for 2 seconds
        else: #Checks to see if the players inputed something random other than "Y" or "N"
            print("Please type in Y or N.") #Tells the players that they need to type in Y or N in order to get a result
print("Thanks for playing!  Type quit() to exit.") #Goodbye message which the player can only see if they us cmd or terminal (which would tell them how to get out of the python interpreter as well) or their program takes a very long time to exit.
quit() #Exits game (if they used cmd or terminal, they still need to exit using the above statement which only appears to those who run this on cmd or terminal)
