# 프로그래밍 패러다임 2가지
#1. 절차지향 -> C, Rudy,...
#2. 객체지향 -> 파이썬, 자바, C++, ...

#객체지향 class = 틀, 현실흉내, (붕어빵 틀)
# class human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def speech(self, text):
#         print(self.name, ":", text)
#
#     #소멸자
#     def __del__(self):
#         print(self.name, '니의 죽음을 알리지 말라')
#
# h1 = Human('홍길동', 20, '남자')
# h2 = Human('아무개', 20, '여자')
#
# h1.speech('안녕하세요') #speech(h1, '안녕하세요')
# h2.speech('반갑습니다') #speech(h2, '반갑습니다')
# # #instance = 실체, (붕어빵)
#
# class OMG:
#     def print(self):
#         print("Oh my god")
#
# mystock = OMG()
# mystock.print()




# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code
#
#     def set_name(self, name):
#         self._name = name
#
#     def set_code(self, code):
#         self._name = name
#
#     def get_name(self):
#         return self._name
#
#     def get_code(self):
#         return self._code
#
# a = Stock(None, None)
# a.set_name("삼성전자")
# a.set_code("005930")
# print(a.get_name())
# print(a.get_code())



#random.randint(x,y)
#-> x부터 y 사이의 랜덤한 숫자
import random

class Account:
    count = 0

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bank = "sc은행"
        self.deposit_count = 0
        self.d_history = []     #입금내역
        self.w_history = []     #출금내역

        import random
        first = str(random.randint(0, 999)).rjust(3, '0')
        middle = str(random.randint(0,99)).rjust(2, '0')
        last = str(random.randint(0, 999999)).rjust(6, '0')
        self.acc = f'{first}-{middle}-{last}'
        Account.count += 1

    @classmethod
    def get_accout_num(cls):
        print(cls.count)

    def deposit(self, money):
        if money >= 1:
            self.money += money
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.money += self.money * 0.01
            self.d_history.append('입금:' + str(money)
                                  + ", 잔고:" + str(self.money))

    def withdraw(self, money):
        if self.money < money:
            self.money -= money
            self.w_history.append('출금:' + str(money)
                                  + ", 잔고:" + str(self.money))

    def deposit_history(self):
        for history in self.d_history:
            print(history)

    def withdraw_history(self):
        for history in self.w_history:
            print(history)

    def display_info(self):
        print('은행이름 :',self.bank)
        print('예금주 :',self.name)
        print('계좌번호 :',self.acc)
        print('잔고 :', self.money)

        '''''''''
        s = str(self.money)     #1234567890
        s = s[::-1]             #0987654321
        s = [ s[i:i+3] for i in range(0, len(s), 3) ]      #['098', '765', '432', '1']
                # l = []
                # for i in range(0, len(S), 3):
                #     l.append(s[i:i+3])
        s = ','.join(s)     # '098, 765, 432, 1'
        s = s[::-1]         # '1, 234, 567, 890'
        print('잔고:', s)
        '''''''''''''''

        print(f'잔고: {self.money :,}')
        # print('잔고:', self.money)


# a = Account('파이썬', 500)
# a.display_info()
# a.deposit(100)
# a.deposit(100)
# a.deposit(100)
# a.deposit(100)
# a.deposit(100)
# print(a.money)

account_list = [ Account('홍길동', 100),
                 Account('아무개', 200),
                 Account('이순신', 3000000)]

for account in account_list:
    if account.money >= 1000000:
        account.display_info






