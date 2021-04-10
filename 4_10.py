#file i/o
#절대경로, 상대경로
#/home/namgil/test.txt
#../namgil/test.txt
#트리 구

# f = open('gt', 'r')
# lines = f.readlines()
# for line in lines:
#     temp = line.split('\n')[0]
#     id, pwd = temp.split(',')
#     print(id, pwd)


#입력값은 id, pwd
#return False or True

input_id = input("Enter the id : ")
input_pwd = input("Enter the pwd : ")

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
flag = login_check(input_id, input_pwd)
if flag:
    print('success')
else:
    print('fail')
