from random import randrange

def display_board(board):
    print("----------")
    for i in range(3):
        print("")
        print(board[i][0], board[i][1], board[i][2], sep='   ')
            
        
        
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):
    print("Enter your move: ")
    move = str(input())
    counter = 0
    for i in range(3):
        for j in range(3):
            counter += 1
            if counter == int(move):
                if board[i][j] == int(move):
                    board[i][j] = 'O'
                else:
                    print("Filled Slot!")
                    enter_move(board)
            else:
                continue
                
                
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    counter = 0
    listed = []
    for i in range(3):
        for j in range(3):
            counter += 1
            if board[i][j] == counter:
                keklist= [i, j]
                listed.append(keklist)
            else:
                continue
    
    return tuple(listed) 
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    for i in range(3):
        if board[i][1] == sign:
            if (board[i][1] == board[i][2] == board[i][0]):
                return True
            else:
                continue
        else:
            continue
        
    for j in range(3):
        if board[0][j] == sign:
            if (board[0][j] == board[1][j] == board[2][j]):
                return True
            else:
                continue
        else:
            continue
        
    if (board[0][0] == board[1][1] == board[2][2] == sign):
        return True
    if (board[0][2] == board[1][1] == board[2][0] == sign):
        return True
        
    return False
    
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    counter=0
    move = randrange(10)
    for i in range(3):
        for j in range(3):
            counter += 1
            if counter == int(move):
                if board[i][j] == int(move):
                    board[i][j] = 'X'
                else:
                    draw_move(board)
            else:
                continue
    # The function draws the computer's move and updates the board.
board = [[1,2,3], [4,'X',6], [7,8,9]]
while True:
    mytuple = make_list_of_free_fields(board)
    if len(mytuple) == 0:
        print("Game Over")
        break
    display_board(board)
    enter_move(board)
    display_board(board)
    draw_move(board)
    display_board(board)
    if victory_for(board,'X'):
        print("Computer Won!")
        break
    elif victory_for(board,'O'):
        print("You won!")
        break
    else:
        continue
    
    
    
    
    
    
    #print(make_list_of_free_fields(board))
    #mytuple = make_list_of_free_fields()
    #if not mytuple:
    #    print("DRAW!")
    #    break


