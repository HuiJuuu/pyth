
def make_map():
    game_map = []

    for i in range (9):
        game_map.append(" _ ")
    return game_map

def print_map(game_map):
    print('-----------')
    print(game_map[0]+'|'+game_map[1]+'|'+game_map[2])
    print('-----------')
    print(game_map[3]+'|'+game_map[4]+'|'+game_map[5])
    print('-----------')
    print(game_map[6]+'|'+game_map[7]+'|'+game_map[8])
    print('-----------')

def check_win(map):
    check = False
    if map[0] == map[1] == map[2]:
        check = True
    elif map[3] == map[4] == map[5]:
        check = True
    elif map[6] == map[7] == map[8]:
        check = True
    elif map[1] == map[4] == map[7]:
        check = True
    elif map[0] == map[3] == map[6]:
        check = True
    elif map[2] == map[5] == map[8]:
        check = True
    elif map[0] == map[4] == map[8]:
        check = True
    elif map[2] == map[4] == map[6]:
        check = True
    return check


game_map = make_map()


print_map(game_map)
a = ' O '
b = ' X '

turn = 0

import random
for i in range(9):

    if turn == 0:
        while True:
            num = int(input("Enter the position : "))
            if game_map[num] == " _ "
                game_map[num] = a
                break
        turn = 1
    else:
        while True:
            num = random.randage(0,8)
            if game_map[num] == " _ ":
                game_map[num] = b
                break
        turn = 0
    print("--------------------again")
    print_map(game_map)
    game_win_check = check_win(game_map)
    if game_win_check:
        break
# while True:
#     num = int(input("Enter the position : "))
#     if turn == 1:
#         if game_map[num] == " _ ":
#             game_map[num] = a
#             turn = 2
#
#         elif game_map[num] == a or game_map[num] == b:
#             turn = 1
#         elif game_win(a):
#             break
#
#         print_map(game_map)
#
#
#     else:
#
#         if game_map[num] == " _ ":
#
#             game_map[num] = b
#
#             turn = 1
#
#         elif game_map[num] == a or game_map[num] == b:
#
#             turn = 2
#
#         elif game_win(a):
#
#             break
#
#         print_map(game_map)

# game_map[0] == a and game_map[1] == a and game_map[2] == a
#game_map[0] == a and game_map[1] == a and game_map[2] == a

# game_map[0] == b and game_map[1] == b and game_map[2] == b
# game_map[3] == b and game_map[4] == b and game_map[5] == b
# game_map[6] == b and game_map[7] == b and game_map[8] == b
# game_map[1] == b and game_map[4] == b and game_map[7] == b
# game_map[0] == b and game_map[3] == b and game_map[6] == b
# game_map[2] == b and game_map[5] == b and game_map[8] == b
# game_map[0] == b and game_map[4] == b and game_map[8] == b
# game_map[2] == b and game_map[4] == b and game_map[6] == b