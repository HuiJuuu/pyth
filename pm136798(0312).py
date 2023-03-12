def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        a = 0
        for j in range(1,i+1):
            if i%j == 0:
                a += 1
        if a > limit:
            answer += power
        else:
            answer += a
    return answer

#약수 빨리 구하기
def PrimeCount(n):
    divisior = set() #집합 - 중복 값 삭제
    for i in range(i, int(n**0.5)+1):
        if n % i == 0:
            divisior.add(i)
            divisior.add(n//i)
    return len(divisior)
