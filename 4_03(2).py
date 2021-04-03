# f = open("gt", 'r')
# 변수 =   (텍스트파일이름, 실행명령)
# Lines = f.readlines()
# 변수   =
# for Line in Lines:
#     print(Line)
# ---------------------------
f = open("gt", 'r')

lines = f.readlines()

for line in lines:
    temp = line.split(',')
    print(temp)
#\n은 줄바꿈