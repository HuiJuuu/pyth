
# n = int(input())
#
# a = list(map(int, input().split()))
#
# nu = a[0]
# bb = a[0]
#
# for i in range(1, n):
#     if nu + a[i] >= bb:
#         bb = nu + a[i]
#     nu = nu + a[i]
#     if nu + a[i] < 0:
#         nu = 0

# n+(n-1)+(n-2)+...+(n-n)
#  2, 3, ..., n개씩 묶기
#  더한값 비교
#  최대값 출력


E = 0
M, F, N = map(int, input().split())
for i in range( ):
    if N > M:
        if N >= F > 1:
            E = E + 1
            N = N - (M-1)
        if N <= 0:
            break
print(E)

