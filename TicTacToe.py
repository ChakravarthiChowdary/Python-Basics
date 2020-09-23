import random


def display_game_board(gameboard):
    print(' ' + gameboard[7] + ' | ' + gameboard[8] + ' | ' + gameboard[9])
    print(' ' + gameboard[4] + ' | ' + gameboard[5] + ' | ' + gameboard[6])
    print(' ' + gameboard[1] + ' | ' + gameboard[2] + ' | ' + gameboard[3])


def player_input():
    symbol = ''

    while not (symbol == 'X' or symbol == 'O'):
        symbol = input('Player 1: Do you want to be X or O? ').upper()

    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_symbol(gameboard, symbol, position):
    gameboard[position] = symbol


def game_win_check(gameboard, mark):

    return ((gameboard[7] == gameboard[8] == gameboard[9] == mark) or
            (gameboard[4] == gameboard[5] == gameboard[6] == mark) or
            (gameboard[1] == gameboard[2] == gameboard[3] == mark) or
            (gameboard[7] == gameboard[4] == gameboard[1] == mark) or
            (gameboard[8] == gameboard[5] == gameboard[2] == mark) or
            (gameboard[9] == gameboard[6] == gameboard[3] == mark) or
            (gameboard[7] == gameboard[5] == gameboard[3] == mark) or
            (gameboard[9] == gameboard[5] == gameboard[1] == mark))


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def player_choice(gameboard, player):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(gameboard, position):
        position = int(input(f'{player} : Choose your next position: (1-9) '))

    return position


def space_check(gameboard, position):
    return gameboard[position] == ' '


def full_gameboard_check(gameboard):
    for i in range(1, 10):
        if space_check(gameboard, i):
            return False
    return True


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    gameBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    game_ready = input('Are you ready to play? Enter Yes or No.')

    if game_ready.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_game_board(gameBoard)
            position = player_choice(gameBoard, turn)
            place_symbol(gameBoard, player1_marker, position)

            if game_win_check(gameBoard, player1_marker):
                display_game_board(gameBoard)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_gameboard_check(gameBoard):
                    display_game_board(gameBoard)
                    print('This is a draw game!')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_game_board(gameBoard)
            position = player_choice(gameBoard, turn)
            place_symbol(gameBoard, player2_marker, position)
            if game_win_check(gameBoard, player2_marker):
                display_game_board(gameBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_gameboard_check(gameBoard):
                    display_game_board(gameBoard)
                    print('This is a draw game!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
