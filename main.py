import math
import random
import time

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
aiPlayer = 'O'
humanPlayer = "X"
emptyCell = '-'
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


# minimax algorithm
def minimax(var_board, is_maximizing, depth=0):
    global aiPlayer
    global humanPlayer
    global emptyCell
    if check_which_player_won(aiPlayer):
        return -100
    elif check_which_player_won(humanPlayer):
        return 100
    elif check_tie():
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if var_board[i] == emptyCell:
                var_board[i] = aiPlayer
                score = minimax(var_board, False)
                var_board[i] = emptyCell
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if var_board[i] == emptyCell:
                var_board[i] = humanPlayer
                score = minimax(var_board, True)
                var_board[i] = emptyCell
                best_score = min(score, best_score)
        return best_score


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
    global aiPlayer
    global currentPlayer
    global emptyCell
    global board
    best_score = math.inf
    best_move = None

    for i in range(9):
        if board[i] == emptyCell:
            board[i] = aiPlayer
            score = minimax(board, False)
            board[i] = emptyCell
            if score < best_score:
                best_score = score
                best_move = i
    print(f"Computer chose {best_move + 1}")
    board[best_move] = aiPlayer


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


def check_which_player_won(mark):
    if board[0] == board[1] == board[2] == mark:
        return True
    elif board[3] == board[4] == board[5] == mark:
        return True
    elif board[6] == board[7] == board[8] == mark:
        return True
    elif board[0] == board[3] == board[6] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[0] == board[4] == board[8] == mark:
        return True
    elif board[2] == board[4] == board[6] == mark:
        return True
    else:
        return False


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
    # switch_player()
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
