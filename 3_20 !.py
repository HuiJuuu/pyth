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

game_map = make_map()

print_map(game_map)
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

# game_map[0] == a and game_map[1] == a and game_map[2]
# game_map[3] == a and game_map[4] == a and game_map[5]
# game_map[6] == a and game_map[7] == a and game_map[8]
# game_map[1] == a and game_map[4] == a and game_map[7]
# game_map[0] == a and game_map[3] == a and game_map[6]
# game_map[2] == a and game_map[5] == a and game_map[8]
# game_map[0] == a and game_map[4] == a and game_map[8]
# game_map[2] == a and game_map[4] == a and game_map[6]

# game_map[0] == b and game_map[1] == b and game_map[2]
# game_map[3] == b and game_map[4] == b and game_map[5]
# game_map[6] == b and game_map[7] == b and game_map[8]
# game_map[1] == b and game_map[4] == b and game_map[7]
# game_map[0] == b and game_map[3] == b and game_map[6]
# game_map[2] == b and game_map[5] == b and game_map[8]
# game_map[0] == b and game_map[4] == b and game_map[8]
# game_map[2] == b and game_map[4] == b and game_map[6]