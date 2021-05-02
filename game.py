#global variables
board = ['-', '-', '-', '-', '-', '-', '-', '-' ,'-']
game_still_going = True
current_player = 'X'
winner = None


def display_board():
    print(board[0], '|', board[1], '|', board[2])
    print(board[3], '|', board[4], '|', board[5])
    print(board[6], '|', board[7], '|', board[8])


def play():
    display_board()

    #make that cyclic
    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == 'X' or winner == 'O':
        print(winner, 'won')
    else:
        print('It\'s a tie')


def handle_turn(player):
    print(player, '\'s turn')
    position = input('Enter postion from 1 to 9: ')
    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Enter postion from 1 to 9: ')

        position = int(position) - 1
        if board[position] != '-':
            print('You cannot go there! Try again ')
        else:
            valid = True
    board[position] = player
    display_board()


def check_if_game_over():
    check_for_win()
    check_for_tie()


def check_for_win():
    global winner

    column_winner = check_for_columns()
    row_winner = check_for_rows()
    diag_winner = check_for_diagonals()

    if column_winner:
        winner = column_winner
    elif row_winner:
        winner = row_winner
    elif diag_winner:
        winner = diag_winner


def check_for_columns():
    global game_still_going

    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'

    if col1 or col2 or col3:
        game_still_going = False

    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]


def check_for_rows():
    global game_still_going

    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    if row1 or row2 or row3:
        game_still_going = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]


def check_for_diagonals():
    global game_still_going

    diag1 = board[0] == board[4] == board[8] != '-'
    diag2 = board[6] == board[4] == board[2] != '-'

    if diag1 or diag2:
        game_still_going = False

    if diag1:
        return board[0]
    elif diag2:
        return board[6]


def check_for_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'


if __name__ == '__main__':
    play()