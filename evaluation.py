import numpy as np


oneDims = [0,
    ' ',' O ',' ',
    ' ',' X ',' ',
    ' ',' ',' '
]


def printBoard(array):
    print(array[1],' | ',array[2],' | ',array[3])
    print(array[4],' | ',array[5],' | ',array[6])
    print(array[7],' | ',array[8],' | ',array[9])
    print()


def emptyIndex(array):
    indexes = []
    for I in range(0,len(array)):
        if array[I] == ' ':
            indexes.append(I)
    print(indexes)
    return indexes 


def moveGen(board,move):
    empty = emptyIndex(board)
    possibilities = []
    boardCopy = board
    for item in empty:
        boardCopy = board.copy()
        boardCopy[item] = move
        possibilities.append(boardCopy)
    for i in range(0,len(possibilities)):
        printBoard(possibilities[i])
        print(i)
moveGen(oneDims,'X')
