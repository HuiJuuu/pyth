a = input()
b = input()
c = a +','+ b
f = open('gt', 'a+')
lines = f.readlines()
new = f.write('\n'+c)
for line in lines:
    temp = line.split('\n')[0]
    id, pwd = temp.split(',')

        print('already exist')

print(id)


# a = "bbbb"
# c = "dddd"
#
# print(a + c)