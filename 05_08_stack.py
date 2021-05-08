# a = [1, 2]
# len(a)
#
# del a[1]
#   data,position = pop(stack,position)
# print('stack', stack)
# print('data', data)
# print('position', position)

def push(stack, data, max_length):
    if len(stack) < max_length:
        stack.append(data)

    else:
        print("over flow")

    return stack

def pop(stack, data):
    if len(stack) > 0:
        del stack[data]

    else:
        print("under flow")

    return stack


max_length = 3
stack = []

while True:

    que = input("Enter push or pop : ")

    if que == "push":
        data = int(input("Enter your number : "))
        stack = push(stack, data, max_length)

    elif que == "pop":
        data =
        stack = pop(stack, data)
