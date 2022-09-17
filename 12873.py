import sys
from collections import deque

#참가자 수를 입력받는다
n = int(sys.stdin.readline())

#참가자 수 만큼 1번부터 N번까지의 번호를 큐에 추가한다.
queue = deque([num for num in range(1, n+1)])

#현재 단계
t = 1

#참가자 한명이 남을때 까지 반복
while len(queue) != 1:
    #큐의 맨 앞에 위치하게 될 참가자의 인덱스 계산
    k = t**3 % len(queue)

    #해당 참가자가 맨 앞에 오도록 큐를 회전
    for i in range(k):
        x = queue.popleft()
        queue.append(x)

    #큐의 맨 뒤에 있는 값을 버린다.
    queue.pop()

    t += 1
#마지막 하나 남은 값 출력
print(queue[0])

