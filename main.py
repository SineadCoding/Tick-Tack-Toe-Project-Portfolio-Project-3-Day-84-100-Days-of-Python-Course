print('Welcome to Tic Tac Toe! #')
print('Player 1 will be Naughts (O) and player 2 will be Crosses (X)')

def board():
    print(f'{pos[0]} | {pos[1]} | {pos[2]}\n'
          f'---------\n'
          f'{pos[3]} | {pos[4]} | {pos[5]}\n'
          f'---------\n'
          f'{pos[6]} | {pos[7]} | {pos[8]}\n')

pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

board()

player1 = True
bar1 = bar2 = []

for num in range(9):
    try:
        if player1:
            bar = int(input('Player one please choose a position for your first mark (type in a number 1-9)')) - 1
            if bar in bar2:
                print('\nPosition already filled')
            else:
                bar1.append(bar)
                pos[bar] = 'X'
                board()
                player1 = False

        else:
            bar = int(input('Player two please choose a position for your first mark (type in a number 1-9)')) -1
            if bar in bar1:
                print('\n {n+1} position already filled')
            else:
                bar2.append(bar)
                pos[bar] = 'O'
                board()
                player1 = True
    except ValueError:
        print('\nNo position has been chosen!')
    except IndexError:
        print('\n Position does not exist!')

    win = [pos[0] == pos[1] == pos[2], pos[3] == pos[4] == pos[5],
           pos[6] == pos[7] == pos[8], pos[0] == pos[3] == pos[6],
           pos[1] == pos[4] == pos[7], pos[2] == pos[5] == pos[8],
           pos[0] == pos[4] == pos[8], pos[2] == pos[4] == pos[6]]

    if pos[0] == pos[1] == pos[2] or pos[3] == pos[4] == pos[5] or pos[6] == pos[7] == pos[8] or pos[0] == pos[3] == pos[6] or pos[1] == pos[4] == pos[7] or pos[2] == pos[5] == pos[8] or pos[0] == pos[4] == pos[8] or pos[2] == pos[4] == pos[6]:
        if player1:
            print("O Wins!!!")
        else:
            print("X Wins!!!")
        break
    elif num == 8:
        print("It's a draw!!!")
