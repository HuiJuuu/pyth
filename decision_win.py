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