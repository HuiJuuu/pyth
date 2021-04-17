#10, 50, 100, 500
#입력 거스름 돈
#출력 동전의 수

a = 10
b = 50
c = 100
d = 500

coin = int(input("Enter the change : "))
n = 0

while coin == 0:
    if coin >= d:
        coin = coin - d
        n = n+1

    elif coin >= c:
        coin = coin - c
        n = n+1

    elif coin >= b:
        coin = coin - b
        n = n+1

    elif coin >= a:
        coin = coin - a
        n = n+1

    print(n)


