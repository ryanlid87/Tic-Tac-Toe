import random

def drawBoard(board):
      # This function prints out the board that it was passed.
 
      # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def CheckWin(board):
    ways = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[7,4,1],[8,5,2],[9,6,3]]
    for blocks in ways:
        if board[blocks[0]] == board[blocks[1]] == board[blocks[2]] and board[blocks[0]] != ' ':
            return board[blocks[0]] + " wins!"
        else:
            return 'yay'

def xPlace(board):
    where = input("Which spot would you like to place an X? 1-9: ")
    if board[int(where)] != ' ':
        print 'This spot is already taken'
        xPlace(board)
    else:
        board[int(where)] = 'X'
        return drawBoard(board)
def oPlace(board):
    where = input("Which spot would you like to place an O? 1-9: ")
    if board[int(where)] != ' ':
        print 'This spot is already taken'
        oPlace(board)
    else:
        board[int(where)] = 'O'
        return drawBoard(board)
def main():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    drawBoard(board)
    while CheckWin(board) == 'yay':
        xPlace(board)
        oPlace(board)
        CheckWin(board)
