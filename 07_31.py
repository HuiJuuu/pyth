# #133
a = ["A", "B", "C"]
i = 0
while i < len(a):
    print(a[i])
    i += 1

# #136
for i in range(1)0, 31, 10):
    print(i)

# #138
for i in range(10,31,10):
    print(i)
    print('------')

# #141
a = [100, 200, 300]
for i in a:
    print(i + 10)

# #143
list = ['SK하이닉스', '삼성전자', 'LG전자']
for i in list:
    print(len(i))

# #144
list = ['dog', 'cat', 'parrot']
for i in list:
    print(f"{i} {len(i)}")

# #145
l = ['dog', 'cat', 'parrot']
for i in l:
    print(i[0])

#151
l = [3, -20, -3, 44]
for i in l:
    if i < 0:
        print(i)

# #152
l = [3, 100, 23, 44]
for i in l:
    if i % 3 == 0:
        print(i)

# #153
l = [13, 21, 12, 14, 30, 18]
for i in l:
    if i % 3 == 0 and i < 20:
        print(i)

# #154
l = ["I", "study", "python", "language", "!"]
for i in l:
    if len(i) >= 3:
        print(i)

# #155
l = ["A", "b", "c", "D"]
for i in l:
    if i.isupper():
        print(i)

#157
l = ["dog", "cat", "parrot"]
for i in l:
    if i[0].islower():
        print(i[0].upper() + i[1:])
        print(i.capitalize())

#158
l = ["hello.py", "ex01.py", "intro.hwp"]
for i in l:
    print(i.split(".")[0])

#159
l = ["intra.h", "intra.c", "define.h", "run.py"]
for i in l:
    if i.split("."):
        if ("h") in i:
            print(i)

# #160
l = ["intra.h", "intra.c", "define.h", "run.py"]
for i in l:
    if i.split(".")[1] in ('h', 'c'):
        print(i)

#B.J.
#구구단
a = int(input())
for i in (1, 10):
    print(f"{a} * {i} = {a * i}")

#10950
T = int(input())
for i in range(T):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a + b)

#8393
n = int(input())
print(int((n + 1) * n / 2))

s = 0
for i in range(1, n + 1):
    s += i
print(s)

#2741
N = int(input())
for i in range(N, 0, -1):
    print(i)

#11021
T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a} + {b} = {a + b}")

#2438
N = int(input())

for i in range (N+1):
    print("*" * i)

#2439
N = int(input())
a = N
for i in range(N+1):
    print((" "*(a-i))+("*" * i))

#10871
N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in A:
    if i < X:
        print(i)
        print(i, end=" ")
