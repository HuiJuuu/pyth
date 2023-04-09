# def solution(N, stages):
#     answer = []
#     fail = []
#     info = [0] * (N + 2)
#     for stage in stages:
#         info[stage] += 1
#     for i in range(N):
#         be = sum(info[(i + 1):])
#         yet = info[i + 1]
#         if be == 0:
#             fail.append((str(i + 1), 0))
#         else:
#             fail.append((str(i + 1), yet / be))
#     for item in sorted(fail, key=lambda x: x[1], reverse=True):
#         answer.append(int(item[0]))
#     return answer






def solution(N, stages):
    info = {}
    p = len(stages)
    failure = []
    answer = []
    for i in range(N): # stage를 key값에 오름차순으로 가진 딕셔너리 생성
        info[i+1] = 0

    for stage in stages:    # info 딕셔너리에 스테이지별 인원 추가
        if stage in info:
            info[stage] += 1

    for k,v in info.items(): # 실패율 구하기
        if k <= N:
            failure.append([k, v/p])
            p -= v  # 앞선 스테이지 도전 중인 인원 빼주기
    print(failure)
    failure.sort(key=lambda x: x[1], reverse=True)

    for i in range(N):
        answer.append(failure[i][0])
    # for i in range(1, N+1):
    #     if i not in info.keys():
    #         failure.append([i, 0])
    # for k in failure:
    #     answer.append(k[0])
    print(answer)
    return answer

solution(5,[2, 1, 2, 6, 2, 4, 3, 3])