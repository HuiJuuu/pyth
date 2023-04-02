def solution(id_list, report, k):
    a = [0]*len(id_list)
    b = {} # 누구를 누가 신고했는지 # key:신고당한, value:신고한
    c = {} # 누가 누굴 신고했는지
    for i in id_list:
        b[i]=[]
        c[i]=[]
    for j in set(report): # 형변환으로 중복신고 거름
        j = j.split(' ')
        b[j[1]].append(j[0])
        c[j[0]].append(j[1])
    print(b)
    print(c)

    # for key.value in a.items():
    #         if s in b:
    #             s >= k
    #             a[id_list.index()] += 1
    count = 0
    for v,s in b.items():
        print(s)
        if len(s) >= k:
            if 
            for i in s:
                continue


        #count += 1

    return a
solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)
#solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"],3)