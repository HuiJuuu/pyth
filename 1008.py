# 1.이진수 소수 -> 십진수 소수 변환기
# 정수를 제외한 소수점 밑의 이진수 숫자들만 입력하여 십진수 소수로 변환 및 출력
# 이진수 x.011은 011로 입력하고 출력은 0.375로 한다.
# 0.011 = 0*2^(-1) + 1*2^(-2) + 1*2^(-3)
# = 0*(1/2) + 1*(1/4) + 1*(1/8)
# = 0 + 0.25 + 0.125
# = 0.375

# a = input()
# b = int(a.split(".")[1])
#
# for i in len(b):
#     b[i-1]*2

def point_btod(binary):
    decimal = 0
    for i, bit in enumerate(binary):
        decimal += int(bit) * (2**-(i+1))
    return decimal
binary = input()
print(point_btod(binary))

# 2. 십진수 소수 -> 이진수 소수 변환기
# 소수점 밑의 십진수 숫자들만 입력하여 이진수 소수로 변환 및 출력
# 생성된 이진수 자릿수가 23자리가 되는 경우 변환을 멈춤
# 모든 숫자 연산은 정수 연산으로 이루어져야 함
# 375 * 2 = 750 --> 0
# 750 * 2 = 1500 --> 1
# 500 * 2 = 1000 --> 1
def point_dtob(decimal):
    # 소수부를 정수로 계산하기 위해 소수부의 제수를 구한다
    divisor = 10
    while divisor < decimal:
        divisor *= 10
    binary = ""
    while decimal > 0 and len(binary) < 23:
        # 소수부 * 2
        decimal *= 2
        # 정수부를 구하여 이진수 자릿수로 추가
        binary += str(decimal // divisor)
        # 정수부를 제외 시킴
        decimal %= divisor

    return binary

decimal = int(input())
print(point_btod(decimal))


# 컴퓨터에서의 실수 표현
# 컴퓨터에서 실수(정수 및 소수)를 표현하는 방식은
# 정수를 표현하는 방식보다 복잡하다. 마찬가지로 이진법을 사용하기 때문이다.
# 또한, 실수 범위의 정확한 값을 표현하는 방법도 없다.

# 고정 소수점(fixed point)
# 실수는 보통, 정수부와 소수부로 나뉘어진다. 따라서 가장 간단한 방식은
# 정수부와 소수부의 자리를 정하고 고정된 자리의 소수를 표현하는 것이다.

# 부동 소수점(floating point)
# 실수의 대부분의 컴퓨터에서는 부동 소수점 방식을 사용하고 있까.
# 여기서 부동은 움직이지 않는다는 뜻의 부동이 아니라 떠다닌다는 뜻의 부동이다.
# 즉, 소수점이 고정되어있지 않고 움직인다는 뜻이다.

# 부동 소수점 방식은 하나의 실수를 부호, 지수부, 가수부(유효수, 분숫값)로
# 나뉘어 표현하고 저장한다. 아래의 그림은 32비트 크기의
# 단정도(single precision) 부동 소수점의 표현을 나타낸다.
# 부호 1bit / 지수부 8bits / 가수부 23bits
# 위와 같은 형태로

# 지수와 바이어스(bias, 편향값)
# 기존 2의 보수를 사용하는 정수 표현 방식은 아래와 같은 특징을 가진다.
# 여기선 지수가 8bits 길이를 가지기 때문에 8bits를 기준으로 설명한다.

# 00000000:0
# 00000001:1
# 00000010:2
# ...
# 01111111:127
# 10000000:-128
# 10000001:-127
# 0부터 시작해서 증가하다가 127을 기준으로 다음 값이 -128로 바뀐다.
# 이제 바이어스 표현법에서는 정수가 어떻게 표현되는지 살펴보자.
# 00000000:-127
# 00000001:-126
# 00000010:-125
# ...
# 01111111:0
# 10000000:1
# 10000001:2
# 바이어스 표현법은 2의 보수와는 전혀 다른 형태로 보인다.
# 원래라면 00000000은 정수 0이어야 하지만 바이어스 표현법에서의
# 00000000은 -127이다 그렇다면 위 값들은..

# 지수부 = E + 127
# 지수 E에 단정도 부동 소수점..

# 그럼 이제 바이어스 표현법을 사용하는 이유를 알아보자. 우선 실수의 크기는 ..

# 이제 부호 S는 0이고 E가 -127인 수와 +127인 수를 대소비교한다고 가정해보자.
# 아래는 지수부에 2의 보수를 사용했을 때다..

# 이렇듯 지수의 제일 작은 음수값인 -127이 0부터 출발하므로 별다를 변환없이
# 비트 검사 만으로도 빠른 대소비교가 가능하다.
# 이게 부동 소수점에서 바이어스 표현법을 사용하는 이유이다.
## 단정도 부돈 소수접에서 bias를 127로 사용하는 이유는 0~255를 가지는..

# 가수
# 가수는 n.nnnnn... 형식으로 나타나는 실수의 유효수이다.
# 가수는 정규화 과정을 거쳐 구해진다.
# 이진수에 대한 정규화를 다루기 전에 먼저 십진수의 경우에 대하여 예를 들겠다.
# 십진수 123.456은 다음과 같이 표기할 수 있다. 여기서 가수는 1.23456에 해당한다.
# ..

# 십진수 32비트 부동 소수점으로 변환하기
# 이제 개념적인 부분은 다 다루었으니, 실전으로 넘어사 425.375를 부동 소수점
# 이진수로 변환하는 과정을 살펴보자.

# 1. 부호비트
# 425.375는 양수다. 그러므로 수식 V = -1^S * M * 2^E에 의하여
# 부호 비트S는 0이다.

# 2. 지수부
# 425.375를 부호없는 이진수로 표현하면 110101001.011이다.
# 여기에 정규화 과정을 거치면 1.10101001011 * 2^8이다.
# 이때 구해진 지수 E는 8이고..

# 3. 가수부
# 위에서 정규화를 통해 구해진 가수는 1.10101001011이다.
# 가수부의 길이는 23바트이므로..

# 32바트 부동 소수점을 십진수로 변환하기
# V = -1^S * M * 2^E를 이용하여 구한다.

# 1. 부호

# 2. 지수

# 3. 가수

# 4. 결과


##파이썬 내장함수
#a = int("0b100") #0b+이진법숫자

class HangulNumber:
    def __init__(self, hangul_num = " 영"):
        self.hangul_num = hangul_num
    def __int__(self):
        num = ""
        for hnum in self.hangul_num:
            if hnum == "영":
                num += 0
            elif hnum == "일":
                num += 1
            elif hnum == "이":
                num += 2
            elif hnum == "삼":
                num += 3
            elif hnum == "사":
                num += 4