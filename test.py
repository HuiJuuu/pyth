import numpy as np

number, day = map(int, input().split())
commute_list = list(map(int, input().split()))
work_max_list = list(map(int, input().split()))
schedule = []

for i, num in enumerate(work_max_list):
    schedule.append([])
    schedule[i].append(num)
    arr = np.array(commute_list)
    indexes = arr.argsort()[::-1][:num]
    for k in indexes:
        if commute_list[k] == 0:
            continue
        schedule[i].append(k + 1)
        commute_list[k] += 1

print(schedule)