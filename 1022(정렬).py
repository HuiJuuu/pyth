#시간 복잡도
# 프로그램의 실행 시간을 나타내는 기호와 수식
# ex) O(N) -> 시간 복잡도가 N이다.
# 결국 코드의 실행 횟수를 의미함

# for i in range(10):
#   sum += i
# 이때의 시간 복잡도는 O(1)
#a(N) = N + 99999999

# for i in range(x):
#    sum += i
# 이때의 시간 복잡도는 O(N)

# for i in range(x):
#    for j in range(y):
#        sum += i
# 이때의 시간 복잡도는 O(N^2)

# for i in range(x):
#    sum += i
# for j in range(y):
#    sum += i
# 이때의 시간복잡도는 O(N)

#공간 복잡도
# 프로그램 실행시 사용되는 메모리의 크기

#1. 선택정렬(selection sort)
# 레코드에서 가장 작은 원소를 찾아 첫 번째 원소와 교환하고
# 두 번째 작은 원소와 교환하고 이러한 방식으로 전체가 정렬될 때까지 계속
# def selection_sort(A):
# for i in range(len(A)):
#     k = i
#     for j in range(i+1, len(A)):
#         if A[k] > A[j]:
# ...

#2. 버블정렬 (bubble sort) (사용 x -> 값 할당이 많이 필요)
# 마치 거품이 물 위로 올라오는 것 같이 루프를
# 한번 반복할 때마다 가장 큰 값을 가진 원소가 가장 뒤쪽으로 이동한다.

#3. 삽입정렬 (사용 X)
# 카드 놀이를 할 때 손에 들고 있는 카드를 정렬하는 것과 유사
# 오른쪽으로 이동하며 차례로 원소를 적절한 위치에 삽입하고 나머지 원소는 하나씩 오른쪽으로 이동시킨다.

#4. 퀵 정렬 (중요)
# 1960년 찰스 안토니 리차드 호어에 의해 개발된 정렬 알고리즘
# 분할 정복 기법을 사용한 정렬 방법의 하나로 현재 가장 광범위하게 쓰이는 정렬 알고리즘
# 퀵 정렬을 개선하려는 시도가 있었지만 큰 성과를 거두지 못함

# 평균적으로 아주 좋은 성능, 약간의 작은 호출 스택 공간만 있으면 별도 메모리 요구 X
# 시간복잡도 O(Nlog2^N)

def quick_sort(A, left, right):
    if right - left <1: #원소의 개수가 1보다 작으면 리턴
        return
    p = A[(left + right) // 2] # 피벗(중간)값 선택
    i = left # left 위치
    j = right # right 위치
    while i < j:# left, right가 만나거나 교차하기 전까지 반복
        while A[i] < p: # 피벗보다 큰 A[i]를 찾음
            j += 1
        while A[i] > p:  # 피벗보다 작은 A[i]를 찾음
            j -= 1
        A[i], A[j] = A[j], A[i] # 두 값을 교환함

    quick_sort(A, left, i - 1) # 남은 부분이 2 이상이면 퀵 소트
    quick_sort(A, j + 1, right) # 남은 부분에 대해 퀵 소트

A = [3, 9, 2, 8, 5, 1, 6, 4, 7]
quick_sort(A< 0, len(A) - 1)
print(A)

#5. 합병 정렬(merge sort)
#