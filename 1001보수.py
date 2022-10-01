#11010 == 26
#110100 == 52

# binary = input()
#
# decimal = 0
# for i, bit in enumerate(reversed(binary)):
#     decimal += int(bit)
# ...
#52 == 110100

# decimal = int(input())
#
# binary = ""
# while decimal > 0:
#     binary += str(decimal % 2)
#     decimal = decimal // 2
#
# binary = binary[::-1]
# print(binary)

# a = input()
#
# for i in range(len(a)):
#     print(a[i])


#01101(이진수) -> 10011(보수)

# a = input()
# b = []
# for i in range(len(a)):
#     if a[i] == 1:
#          b.append(0)
#     elif a[i] == 0:
#         b.append(1)
#     print(a[i],b)
#영상

#HINT
#0101(이진수) == 5(십진수)
#2의 보수 취한 1011(이진수) == -5(십진수)
#2의 보수 취한 0101 == 5(십진수)
# => 보수를 취할 때마다 부호가 바뀜

#110111(이진수(2의 보수 사용)) -> -9(십진수)

def binary_to_decimal(binary):
    decimal = 0
    for i, bit in enumerate(binary[::-1]):
        decimal += int(bit) *

#이진수 2의 보수
def twos_complement(binary):
    comp1 = ""
    for bit in binary:
        comp1 += "1" if bit == "0" else "0"

    comp2 = ""
    carry_bit = 1
    for bit in comp1[::-1]:
        if bit == "1" and carry_bit == 1:
            comp2 += "0"
        elif bit == "0" and carry_bit == 1:
            comp2 += "1"
            carry_bit = 0
        else:
            comp2 += bit
    return comp2[::-1]

binary = input()

sign = 1 #부호

#최상위 비트가 1이면 2의 보수로 표현된 음수임
if binary[0] == "1":
    #다시 2의 보수를 취하면 이진수 양수임
    binary = twos_complement(binary)
    #부호는 음수
    sign = -1
#이진수를 십진수로 전환
decimal = binary_to_decimal(binary)

#부호를 결정함
decimal = decimal * sign

print(decimal)
