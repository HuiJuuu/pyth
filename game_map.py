def print_map(nk_map):
    print('-----------')
    print(nk_map[0] + '|' + nk_map[1] + '|' + nk_map[2])
    print('-----------')
    print(nk_map[3] + '|' + nk_map[4] + '|' + nk_map[5])
    print('-----------')
    print(nk_map[6] + '|' + nk_map[7] + '|' + nk_map[8])
    print('-----------')

def make_map():
    game_map = []
    for i in range(9):
        game_map.append(' _ ')
    return game_map