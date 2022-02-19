f = open("test.txt", 'r')

#f.write("hi\t")
#f.write("hello")

lines = f.readlines()
print(lines)

f.close()