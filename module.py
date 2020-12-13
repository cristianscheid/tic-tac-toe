import os
os.system('clear')

matrix = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

p_line = [0, 1, 2]
p_column = [0, 1, 2]


def reset_matrix():
    global matrix
    matrix = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]


def print_matrix():
    print('    |-----|-----|-----|')
    for i in matrix:
        print('  ', *i, '\n    |-----|-----|-----|', sep='  |  ')
    print()


def verify_available(value):
    is_available = False
    for i in p_line:
        for j in p_column:
            if matrix[i][j] == value:
                is_available = True
    return is_available


def verify_value(valor):
    is_valid = False
    if 0 < int(valor) < 10:
        is_valid = True
    return is_valid


def verify_win(simbol):
    is_winner = False
    for i in p_line:
      if matrix[i][0] == simbol and matrix[i][1] == simbol and matrix[i][2] == simbol:
        is_winner = True
      elif matrix[0][i] == simbol and matrix[1][i] == simbol and matrix[2][i] == simbol:
        is_winner = True
      elif (matrix[0][0] == simbol and matrix[1][1] == simbol and matrix[2][2] == simbol) or \
              (matrix[0][2] == simbol and matrix[1][1] == simbol and matrix[2][0] == simbol):
        is_winner = True
    return is_winner

def finish_win():
    os.system('clear')
    print_matrix()
    print(check + ' is the winner!')
    print('')
    play_again = input('Wanna play again? (y/n) ')
    if play_again == 'y' or play_again == 'Y':
        count_round = 0
        reset_matrix()
        os.system('clear')
        start()
    elif play_again == 'n' or play_again == 'N':
        print('See you later ;)')

def start():
    count_round = 0
    max_round = 9
    player_of_round = 'X'
    global check
    while count_round < max_round:
        print_matrix()
        choice = input('--> ' + player_of_round + ' turn...\n\n'
                                                  'Round ' + str(count_round + 1) +
                       ' --> Make your play (1-9): ')
        if verify_available(choice) and verify_value(choice):
            if count_round % 2 == 0:
                check = 'X'
                player_of_round = 'O'
            else:
                check = 'O'
                player_of_round = 'X'
            if int(choice) < 4:
                matrix[0][int(choice) - 1] = check
            elif int(choice) < 7:
                matrix[1][int(choice) - 4] = check
            else:
                matrix[2][int(choice) - 7] = check
            if verify_win(check):
                os.system('clear')
                finish_win()
                break
            count_round += 1
        os.system('clear')