def login_check(input_id, input_pwd):
    f = open("gt", 'r')
    lines = f.readlines()
    flag = False
    for line in lines:
        temp = line.split('\n')[0]
        id, pwd = temp.split(',')

        if id == input_id and pwd == input_pwd:
            flag = True
            break
    return flag


f = open('gt', 'a')
f.write('\naaa,bbb')
