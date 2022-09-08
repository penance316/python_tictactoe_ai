board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
aiPlayer = 'O'
humanPlayer = "X"
currentPlayer = humanPlayer
winner = None
gameRunning = True


# print game board
def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('----------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# take players input
def player_input(board):
    global currentPlayer
    input_var = int(input(f"Player {currentPlayer} : Enter a number from 1-9: "))
    if 1 <= input_var <= 9 and board[input_var - 1] == '-':
        board[input_var - 1] = currentPlayer
    else:
        print("Invalid input")


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


# check for win or tie again


while gameRunning:
    print_board(board)
    player_input(board)
    if check_tie():
        print("Tie")
        gameRunning = False
    if check_winner():
        print_board(board)
        print("Player " + winner + " wins!")
        gameRunning = False
    switch_player()
