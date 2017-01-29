#!/usr/local/bin/python3.5
"""Program: Tic-Tac-Toe
Description: PLay Tic-Tac-Toe with the computer
Author: Roni Rengit """

from random import randrange

args = [['', '', ''],
        ['', '', ''],
        ['', '', '']]
i = 0
comp = ''


def board(matrix):

    print("%80.11s" % 'TIC-TAC-TOE')
    print(2 * ' ' + matrix[0][0] + 2 * ' ' + '|' + 2 * ' ' + \
          matrix[0][1] + 2 * ' ' + '|' + \
          2 * ' ' + matrix[0][2] + 2 * ' ')
    print(15 * '-')
    print(2 * ' ' + matrix[1][0] + 2 * ' ' + \
          '|' + 2 * ' ' + matrix[1][1] + 2 * ' ' + '|' + \
          2 * ' ' + matrix[1][2] + 2 * ' ')
    print(15 * '-')
    print(2 * ' ' + matrix[2][0] + 2 * ' ' + '|' + 2 * ' ' + \
          matrix[2][1] + 2 * ' ' + '|' + \
          2 * ' ' + matrix[2][2] + 2 * ' ')


def computer_play(mat):

    global i, comp

    # Location
    x = randrange(0, 3)  # location 1
    y = randrange(0, 3)  # location 2

    # Computer choice
    while i == 0:
        choice = ['x', 'o']
        comp = choice[randrange(0, 2)]  # Choose 'x' or 'o'
        i += 1

    if mat[x][y] == '':
        mat[x][y] = comp
        return board(mat)
    else:
        computer_play(mat)


def player_play(choice):

    # location
    location = {'UL': '00', 'UM': '01', 'UR': '02', \
                'ML': '10', 'MM': '11', 'MR': '12', \
                'LL': '20', 'LM': '21', 'LR': '22'}

    x = input('Enter location(UL, UM, UL, ML, MM, MR, LL, LM, LR):')
    string = location[x]

    # Enter choice
    player_choice = input("'x' or '0'?")
    if choice[int(string[0])][int(string[1])] == '':
        choice[int(string[0])][int(string[1])] = player_choice
        return board(choice)
    else:
        print("Forbidden Move! Try again !!!")
        player_play(choice)


def main():
    for n in range(1, 10):
        if n % 2 == 0:
            player_play(args)
        else:
            computer_play(args)

if __name__ == '__main__':
    main()
else:
    main()
