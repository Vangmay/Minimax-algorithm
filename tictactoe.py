import random
import copy 
board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

Human = 'X'
AI = 'O'

#Scores from X's perspective
Win = 1
Draw = 0
Lose = -1

def displayBoard(board):
    print('--------------------------')
    print(board[0][0] ,'|', board[0][1] ,'|' , board[0][2]) 
    print(board[1][0] ,'|', board[1][1] ,'|', board[1][2]) 
    print(board[2][0] ,'|', board[2][1] ,'|', board[2][2]) 
    print('--------------------------')
def availabile(board):
    empty = []
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j] == ' ':
                spot = [i,j]
                empty.append(spot)
    return empty

def playerInput(board,sign=Human):
    print('Executing playerInput')
    spot = []
    availabileSpots = availabile(board)

    i = int(input("Input row : "))
    j = int(input("Input column : "))
    spot = [i,j]
    if spot in availabileSpots:
        board[i][j] = sign 
    else:
        print("The spot you chose was not empty, please chose another spot")
        playerInput(board,sign)
    return(board)
# playerInput(board,'X')
def RobotInput(board,sign=AI):
    print('Executing RobotInput')
    bestScore = -99999999
    bestMove = []
    availabileSpots = availabile(board)
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if (board[i][j] == ' '):
                board[i][j] = AI 
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if(score > bestScore):
                    bestScore = score;
                    bestMove = [i,j]
    board[bestMove[0]][bestMove[1]] = AI 
    return board 
    # index = random.randint(0,len(moves)-1)
    # move = moves[index]
    # board[move[0]][move[1]] = sign
#Minimax-----------------------
def minimax(board, depth, isMaximizing):
    print("Executing Minimax")
    scores = {'X':1 , 'O':-1 , 'Draw':0}
    result = checkWinner(board)
    if (result != ''):
        score = scores[result]
        return score; 
    if isMaximizing:
        bestScore = -9999999
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] == ' ':
                    board[i][j] = AI
                    score = minimax(board,depth+1,False)
                    board[i][j] = ' '
                    if score > bestScore:
                        bestScore = score
        return bestScore
    else:
        bestScore = -9999999
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] == ' ':
                    board[i][j] = Human
                    score = minimax(board,depth+1,True)
                    board[i][j] = ' '
                    if score < bestScore:
                        bestScore = score 
        return bestScore 
    
#Minimax-----------------------
    

def checkWinner(board):
    print('Executing checkwinner')
    win = ''
    # Horizontal
    for i in range(0,3):
        if (board[i][0] == board[i][1] and board[i][0]==board[i][2] and board[i][0] != ' '):
            win = board[i][0]
            return win
    # vertical
    for i in range(0,3):
        if (board[0][i] == board[1][i] and board[0][i]==board[2][i] and board[0][i] != ' '):
            win = board[0][i]
            return win
    if(board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != ' '):
        win = board[0][0]
        return win 
    if(board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != ' '):
        win = board[0][2]
        return win 
    if availabile(board) == [] and win == ' ':
        return 'Draw'
    return win 


#Display board
#Ask for input from human and put it
#Check if win
#Ask for input from robot and put it
#Check if win
#Repeat until win doesn't return anything

def driver(board):
    player = 'Human'
    displayBoard(board)
    while checkWinner(board) == '':
        if player == 'Human':
            playerInput(board)
            checkWinner(board)
            player = 'Robot'
        if player == 'Robot':
            RobotInput(board)
            checkWinner(board)
            player = 'Human'
        displayBoard(board)
    print('The winner is ',checkWinner(board))
driver(board)