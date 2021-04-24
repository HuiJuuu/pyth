from loing_info import login_check
from game_map import print_map, make_map
from decision_win import check_win

input_id = input("Enter the id : ")
input_pwd = input("Enter the pwd : ")

flag = login_check(input_id, input_pwd)
if flag:
    print('success')

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
                num = random.randrange(0, 8)
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

else:
    print('fail')
