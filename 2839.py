n = int(input())

if n >= 5 and n % 3 != 0:
    A = n // 5
    a = n % 5

    if a >= 3:
        B = a // 3
        b = a % 3

        if b == 0:
            print(A + B)
        else:
            print(-1)
    else:
        print(-1)
        
elif n % 3 == 0 :
    aa = n // 3
    print(aa)

else:
    print(-1)