
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


game_map = make_map()
a = ' O '
b = ' X '
turn = 1


while True:
    num = int(input("Enter the position : "))
    if turn == 1:
        if game_map[num] == " _ ":
            game_map[num] = a
            turn = 2

        elif game_map[num] == a or game_map[num] == b:
            turn = 1

        print_map(game_map)

    else:

        if game_map[num] == " _ ":
            game_map[num] = b
            turn = 1

        elif game_map[num] == a or game_map[num] == b:
            turn = 2

        print_map(game_map)

    game_win = check_win(game_map)
    if game_win:
        break

if not game_win:
    print('draw')