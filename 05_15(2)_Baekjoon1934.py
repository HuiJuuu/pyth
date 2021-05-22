t = int(input())
A = int(input())
B = int(input())


for i in range (A, (A*B)+1):
    if i % A == 0 and i % B == 0:
        print(i)
        break
