# #201
# def print_coin():
#
#     print("비트코인")
#
# #202
# print_coin()
#
# #203
# for i in range(100):
#     print_coin()

#204
# def print_coins():
#     for i in range(100):
#         print("비트코인")
#
# print_coins()

#205
#함수가 정의 되기 전에 호출되었다.

#215
# def print_with_smile():
#     a = input()
#     print(a + ":D")
#
# #216
# print_with_smile()

#217
def print_upper_price():
    a = int(input())
    b = a * 1.3
    print(b)

#218
def print_sum():
    a = int(input())
    b = int(input())
    c = a + b
    print(c)

#219
def print_arithmetic_operation(a,b):
    print(f'{a} + {b} = {a+b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} / {b} = {a / b}')
    print(f'{a} * {b} = {a * b}')

print_arimate_operation(3,4)

#220
def print_max(a,b,c):
    if a>= b and a>= c:
        print(a)
    elif b>= a and b>= c:
        print(b)
    else:
        print(c)

#221
def print_reverse(text):
    return text[::-1]
    return''.join(reversed(list(text)))
    result = ''
    for c in text:
        result = c +result
    return result

print(print_reverse('python'))

#223
def print_score(score_list):
    return sum(score_list) / len(score_list)

print(print_score([1, 2, 3]))

#223
def print_even(l):
    result = []
    for i in l:
        if i % 2 == 0:
            result.append(i)

    return result

r = print_even([1, 3, 2, 10, 12, 11, 15])
print(r)

#224
def print_keys(dictionary):
    return list(dictionary.keys())

r = print_keys({"이름":"김말똥", "나이":30, "성별":0})
for i in r:
    print(i)

#226
def print_mxn(string, m):
    i = 0
    for c in string:
        if i % m == 0 and i != 0:
            print()
        print(c, end ='')
        i += 1

print_mxn("아이엠어보이유알어걸", 3)

#228
def calc_monthly_salary(annual_salary):
    return annual_salary // 12

#