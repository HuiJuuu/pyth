
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
a = ' O '
b = ' X '

position = int(input("Enter the your position : "))

turn = 1
while game_map[position] != a and game_map[position] != b:
        if turn == 1:
            game_map[position] = a
            if game_map[position] == a:
                print(position)
            turn = 2
        else:
            game_map[position] = b
            if game_map[position] ==b:
                print(position)
            turn = 1
        print_map(game_map)
