
def make_map():
    game_map = []

    for i in range (9):
        game_map.append(' _ ')
    return game_map

def print_map(nk_map):
    print('-----------')
    print(nk_map[0]+'|'+nk_map[1]+'|'+nk_map[2])
    print('-----------')
    print(nk_map[3]+'|'+nk_map[4]+'|'+nk_map[5])
    print('-----------')
    print(nk_map[6]+'|'+nk_map[7]+'|'+nk_map[8])
    print('-----------')

def check_win(map):
    check = False
    if map[0] == map[1] == map[2] != ' _ ':
        check = True
    elif map[3] == map[4] == map[5] != ' _ ':
        check = True
    elif map[6] == map[7] == map[8] != ' _ ':
        check = True
    elif map[1] == map[4] == map[7] != ' _ ':
        check = True
    elif map[0] == map[3] == map[6] != ' _ ':
        check = True
    elif map[2] == map[5] == map[8] != ' _ ':
        check = True
    elif map[0] == map[4] == map[8] != ' _ ':
        check = True
    elif map[2] == map[4] == map[6] != ' _ ':
        check = True
    return check


a = ' O '
b = ' X '
turn = 0
game_map = make_map()

import random
for i in range(9):
    if turn == 0:
        while True:
            num = int(input("Enter the position : "))
            if game_map[num] == ' _ ':
                game_map[num] = a
                break
        turn = 1
    else:
        while True:
            num = random.randrange(0,8)
            if game_map[num] == ' _ ':
                game_map[num] = b
                break
        turn = 0
    print("--------------------again")
    print_map(game_map)
    game_win_check = check_win(game_map)
    if game_win_check:
        break

if not game_win_check:
    print('draw')
