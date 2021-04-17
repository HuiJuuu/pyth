#1,1,2,3,5,8,13,21,34,55
a = 1
b = 1
p = int(input())

for i in range (p-1):
    a = b
    b = a+b
print(a+b)
