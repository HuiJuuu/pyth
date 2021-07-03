#1
print('HELLO WORLD')

#2
print("Mary's cosmetics")
print('Mary\'s cosmetics')

#3
print('신씨가 소리질렀다. "도둑이야"."')
print("신씨가 소리질렀다. \"도둑이야\".")

#4
print('"C:\\Windows"')
print(r'C:\Windows')

#5
print('"안녕하세요.\n 만나서\t\t반갑습니다."')

#6
print("오늘은", "일요일")

#7
print('naver;kakao;sk;samsung')

#8
print("naver/kakao/sk/samsung")

#9
print("first"); print("second")
print("first", end=" "); print("second")

#10
print(5/3)

#11
SE = 50000
print(SE*10)

#12
total = 298000000000000
present = 50000
PER = 15.79

#13
s = "hello"
t = "python"

print(s+"!"+t)
#print("{}! {}").format(s, t)
print(f"{s}! {t}")
print(f"{'{'}")

#14
print(2+2*3)

#15
a = 128
print(type(a))

b = "132"
print(type(b))

#16
num_str = "720"
num_int = int(num_str)
print(type(num_str), type(num_int))

#17
num = 100
s = str(num)
print(type(num), type(s))

#18
a = "15.79"
b = float(a)
print(type(a), type (b))

#19
year = "2021"
p = int(year)
print(p-2, p-1, p)

#20
m = 48584
t = 36
print(m*t)

#21
letters = 'python'
print(letters[0], letters[2])

#22
license_plate = "24 가 2210"
print(license_plate[5:])
print(license_plate[5:9])
#[시작인덱스 : 끝 인덱스]

#23
string = "홀짝홀짝홀짝"
print(string[0]+string[2]+string[4])
print(string[0:5:2])
print(string[::2])
#[시작인덱스 : 끝 인덱스 : 오프셋]

#24
string = "PYTHON"
print(string[::-1])
print(string[5:0:-1]) #(x)
#역순 출력은 마지막 오프셋만 입력

#25
phone_number = "010-1111-2222"
s = phone_number.replace("-"," ")
print(s)

#26
d = s.replace(" ", "")
print(d)

#27
url = "http://sharebook.kr"
print(url[17:])
splitted = url.split(".")
print(splitted[1])

#28
lang = 'python'
#lang[0] = 'P'
lang = list(lang)
lang[0] = 'P'
lang = ''.join(lang)
print(lang)

#29
string = "abcdefe2a354a32a"
result = string.replace("a", "A")
print(result)

#30
string = 'abcd'
String = string.replace('b', 'B')
print(String)

#31
a = "3"
b = "4"
print(a + b)

#32
print("Hi" * 3)

#33
print('-' * 80)

#34
t1 = 'python'
t2 = 'java'
print((t1 + " " + t2 + " ")*4)

#35
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

#37 (python 3.6 이상)
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

#38
상장주식수 = "5,969,782,550"
a = 상장주식수.replace(",", "")
b = int(a)
print(type(b))

#39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
#[시작 인덱스 : 시작 인덱스 + 1(끝 인덱스)]

#40
data = "    삼성 전자    "
print(data.replace(" ", ""))
print(data.strip())
print(data.lstrip())
print(data.rstrip())