# n = int(input('라운드 : '))
# A = 100
# B = 100
# for i in range(n):
#     # a = int(input())
#     # b = int(input())
#     a, b = map(int, input().split())
#     if a>b:
#         B = B - a
#     elif a<b:
#         A = A - b
#     else:
#         pass
#
#     print('A:', A)
#     print('B:', B)

#stack, list, 3
MAX_LEN = 3
stack = []
def push(stack, data):

    if len(stack) == MAX_LEN:
        print("Overflow")
    else:
        stack.append(data)
    return stack

def pop(stack):

    if len(stack) == 0:
        print("Underflow")
    else:
        print(stack[len(stack) - 1])
        del stack[len(stack) - 1]

    return stack

push(4)
push(2)
pop()
pop()
#init()
#overflow
#underflow

#queue, list, 5
# def enqueue():
#
# def dequeue():
#     pass