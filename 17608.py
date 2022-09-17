
import sys

#막대기의 갯수
n = int(sys.stdin.readline())

# 각 막대기의 길이를 스택에 입력
stack = [int(sys.stdin.readline()) for _ in range(n)]

#보이는 막대기의 개수
count = 0

#막대기의 최대 길이 스택 검사 전이므로 0
max_stick = 0

#스택에서 막대기를 하나씩 빼며 길이를 검사
while stack:
    #스택에서 막대기 하나를 꺼냄
    stick = stack.pop()
    #지금까지 나온 막대기보다 긴 막대기인 경우
    #보이는 막대기임.
    if stick > max_stick:
        max_stick = stick
        count += 1

print(count)




from collections import deque
queue = deque([1, 2, 3])
