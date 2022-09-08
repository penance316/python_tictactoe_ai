import random
import time

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
aiPlayer = 'O'
humanPlayer = "X"
currentPlayer = humanPlayer
winner = None
gameRunning = True


# print game board
def print_board(var_board):
    print(var_board[0] + ' | ' + var_board[1] + ' | ' + var_board[2])
    print('----------')
    print(var_board[3] + ' | ' + var_board[4] + ' | ' + var_board[5])
    print('----------')
    print(var_board[6] + ' | ' + var_board[7] + ' | ' + var_board[8])


# take players input
def player_input(var_board):
    global currentPlayer
    input_var = int(input(f"Player {currentPlayer} : Enter a number from 1-9: "))
    if 1 <= input_var <= 9 and var_board[input_var - 1] == '-':
        var_board[input_var - 1] = currentPlayer
    else:
        print("Invalid input")
        print_board(var_board)
        player_input(var_board)


# Computer moves.
def computer_input():
    global currentPlayer
    global aiPlayer
    while currentPlayer == aiPlayer:
        print("Computer is thinking...")
        time.sleep(1)
        input_var = random.randint(0, 8)
        if board[input_var] == '-':
            board[input_var] = aiPlayer
            switch_player()


# check for win/tie
def check_horizontal():
    global winner
    if board[0] == board[1] == board[2] != '-':
        winner = board[0]
    elif board[3] == board[4] == board[5] != '-':
        winner = board[3]
    elif board[6] == board[7] == board[8] != '-':
        winner = board[6]


def check_vertical():
    global winner
    if board[0] == board[3] == board[6] != '-':
        winner = board[0]
    elif board[1] == board[4] == board[7] != '-':
        winner = board[1]
    elif board[2] == board[5] == board[8] != '-':
        winner = board[2]


def check_diagonal():
    global winner
    if board[0] == board[4] == board[8] != '-':
        winner = board[0]
    elif board[2] == board[4] == board[6] != '-':
        winner = board[2]


def check_tie():
    return '-' not in board


def check_winner():
    global winner
    check_horizontal()
    check_vertical()
    check_diagonal()
    return winner == 'X' or winner == 'O'


# switch player
def switch_player():
    global currentPlayer
    if currentPlayer == humanPlayer:
        currentPlayer = aiPlayer
    elif currentPlayer == aiPlayer:
        currentPlayer = humanPlayer


while gameRunning:
    print_board(board)
    player_input(board)
    if check_tie():
        print("Tie")
        gameRunning = False
        break
    if check_winner():
        print_board(board)
        print("Player " + winner + " wins!")
        gameRunning = False
        break
    switch_player()
    computer_input()
    if check_tie():
        print("Tie")
        gameRunning = False
        break
    if check_winner():
        print_board(board)
        print("Player " + winner + " wins!")
        gameRunning = False
        break
