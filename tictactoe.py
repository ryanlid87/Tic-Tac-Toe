from random import randint 

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
    return 'yay'

def xPlace(board):
    where = input("Which spot would you like to place an X? 1-9: ")
    try:
        if board[int(where)] != ' ':
            print 'This spot is already taken'
            xPlace(board)
        else:
            board[int(where)] = 'X'
            return drawBoard(board)
    except IndexError:
        print 'Thats not a valid spot'
        xPlace(board)

def Think(board):
    ways = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[7,4,1],[8,5,2],[9,6,3]]
    for blocks in ways:
        if board[blocks[0]] == board[blocks[1]] and board[blocks[0]] != ' ' and board[blocks[2]] == ' ':
            return blocks[2]
        if board[blocks[1]] == board[blocks[2]] and board[blocks[1]] != ' ' and board[blocks[0]] != ' ':
            return blocks[0]
        if board[blocks[0]] == board[blocks[2]] and board[blocks[0]] != ' ' and board[blocks[1]] != ' ':
            return blocks[1]
    return randint(1,9)

def oPlace(board):
    where = Think(board)
    if board[where] == ' ':
        board[where] = 'O'
    else:
        randint(1,9)
    return drawBoard(board)

        
def SpacesLeft(board):
    for x in range (1,10):
        if board[x] == ' ':
            return True
    return False

def main():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    drawBoard(board)
    SpacesLeft(board)
    while CheckWin(board) == 'yay' and SpacesLeft(board) == True:
        xPlace(board)
        if CheckWin(board) != 'yay': break
        if SpacesLeft(board) == False:break
        oPlace(board)
        CheckWin(board)
    if SpacesLeft(board) == False:
        print 'It was a tie.'
    else:
        print CheckWin(board)
        
main()


