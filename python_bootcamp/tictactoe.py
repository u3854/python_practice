import subprocess
from time import sleep
import random

def initialize():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return board


# PRINTING CURRENT BOARD
def print_board(board):

	i = 0
	for row in board:
		i += 1
		print('   |   |   ')
		print(' ' + row[0] + ' | ' + row[1] + ' | ' + row[2])
		if i<3:
			print('___|___|___')
		else:
			print('   |   |   \n')

# CHECKING FOR MATCH
def check(board):
    if board[0][0] == board[0][1] == board[0][2]:           # ROW 1
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]:         # ROW 2
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]:         # ROW 3
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0]:         # COLUMN 1
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:         # COLUMN 2
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]:         # COLUMN 3
        return board[0][0]
    elif board[0][0] == board[1][1] == board[2][2]:         # DIAGONAL L2R
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:         # DIAGONAL R2L
        return board[1][1]

# TAKING PLAYER POSITION INPUT
def player_input(board):

    x = input("Enter postion in the format <int>,<int>: ")
    x = x.split(',')
    #print(x,type(x[0]),type(x[1]))
    if len(x) == 2 and x[0].strip() in ['1','2','3'] and x[1].strip() in ['1','2','3'] and board[int(x[0].strip())-1][int(x[1].strip())-1] == ' ':
        return [int(x[0].strip()),int(x[1].strip())]
    else:
        print('Invalid input!')
        return player_input(board)


# UPDATE BOARD AFTER PLAYER INPUT
def board_update(board, x, s):
    board[x[0]-1][x[1]-1] = s
    return board


# CHECK IF PLAYERS WANT TO REPLAY
def game_reset():
    x = input('Good game! Do you want to play again? (Y/N): ')
    if x.lower() == 'y':
        subprocess.run('cls', shell = True)
        game()
    elif x.lower() == 'n':
        subprocess.run('cls', shell = True)
        print('Thank you for playing!')
    else:
        print('Invalid input!')
        game_reset()

# MAIN GAME
def game():

    subprocess.run('cls', shell = True)
    print('TIC-TAC-TOE starting', end = '')
    for i in range(2):
        print('.', end ='', flush = True); sleep(random.randrange(2,4,1))
    print('.\n')
    board = initialize()
    print_board(board)
    print('Player 1 (X) get ready!\n')
    
    i = 0
    sleep(2)

    for i in range(8):

        if i % 2 == 0:
            print('PLAYER 1 (X):')    
            x = player_input(board)
            board = board_update(board, x, 'X')
        else:
            print('PLAYER 2 (O):')    
            x = player_input(board)
            board = board_update(board, x, 'O')

        subprocess.run('cls', shell = True)   
        print_board(board)
        a = check(board)
        
        if a == 'X':
            print('\nPlayer 1 wins!')
            game_reset()
            break
        elif a == 'O':
            print('\nPlayer 2 wins!')
            game_reset()
            break


    if i == 7:              # AUTO-FILLING LAST SPOT ON BOARD
        for u in range(3):
            for v in range(3):
                if board[u][v] == ' ':
                    board[u][v] = 'O'
                    a = check(board)
                    if a == 'X':
                        print('\nPlayer 1 wins!')
                    elif a == 'O':
                        print('\nPlayer 2 wins!')
                    else:
                        print ('\nGame ends in a draw!')
                    game_reset()
        

game()
