
def enq(q, data, max_length):
    if len(q) < max_length:
        q.append(data)

    else:
        print("over flow")

    return q

def deq(q):
    if len(q) > 0:
        del q[0]
    else:
        print('under flow')

    return q


max_length = 3
q = []
len(q)

while True:
    que = input('Enter the enq or deq : ')

    if que == "enq":
        data = int(input("Enter your number : "))
        q = enq(q, data, max_length)
        print(q)

    elif que == "deq":
        q = deq(q)
        print(q)


