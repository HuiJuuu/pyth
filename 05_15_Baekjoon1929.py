#m, n = map(int,input().split())
# a=int(input())
# b=int(input())
#
# for i in range(2,b):
#     if a%i==0 :
#         a = a+1
#     elif a%i!=0:
#         print(a)
#         a = a+1

a=int(input())
b=int(input())
anw=[]
for i in range(a,b+1):
    if i == 2:
        anw.append(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1:
                anw.append(i)

print(anw)