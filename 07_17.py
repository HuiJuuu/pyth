
# a = [1, 2, 3]
# b = (365, 24)
#
# b[0] = 1

#71
my_variable = ()
print(type(my_variable))

#72
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')

#73
t = (1)

#75
t = 1, 2, 3, 4
print(type(t))

#76
t = ('a', 'b', 'c')

#77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(type(interest))

#78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)

#79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

#80
t = []
for i in range(2,101):
    if i%2 == 0:
        t.append(i)
print(t)

t = tuple(t)
print(t)

#80_2
def make_tuple():
    tesst = []
    for i in range(1,100):
        if i % 2 == 0:
            test.append(i)
    test = tuple(test)
    return test

#81
a, b, *c = (0, 1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(valid_score)

#82
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(valid_score)

#83
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, b = scores
print(valid_score)

#84
#key, value
temp = {}
temp = {'a':123, 123: 'c', 'a' :123123123123}

#add dictionary value
temp['b'] = 123
print(temp)

#delete aictionary value
del temp['b']

#key
print(temp.keys())

#
temp = ('a', 'b', 'c')
test = (1, 2, 3)

output = zip(temp,test)
print(dict(output))

#85
ice = {'메로나':1000, '폴라포':1200, '빵빠레':1800}

#86
ice['죠스바'] = 1200
ice['월드콘'] = 1500
print(ice)

#87
print('메로나 가격 :', ice['메로나'])

#88
ice['메로나'] = 1300
print(ice)

#89
del ice['메로나']
print(ice)

#90

#91
inventory = {'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}

#92
print(inventory['메로나'][0])

#93
print(inventory['메로나'][1])

#94
inventory['월드콘'] = [500,7]
print(inventory)

#95
icecream = {'탱크보이':1200, '폴라포':1200, '빵빠레':1000, '월드콘':1500, '메로나':1000}
print(icecream.keys())

#96
print(icecream.values())

#97
print(icecream['탱크보이']+icecream['빵빠레']+icecream['월드콘']*3)

#98
icecream = {'탱크보이':1200, '폴라포':1200, '빵빠레':1000, '월드콘':1500, '메로나':1000}
new_product = {'팥빙수':2700, '아맛나':1000}

icecream.update(new_product)
print(icecream)

#99
keys = ('apple', 'pear', 'peach')

yals = (300, 250, 400)

output = zip(keys,yals)
print(dict(output))

#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10000, 11000]

close_table = zip(date, close_price)
print(dict(close_table))

#101
