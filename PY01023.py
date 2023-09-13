import math

for t in  range(int(input())):
    x = int(input())
    s = 0
    i = 2
    print("1 * ", end = '')
    while(x > 0):
        if(x % i == 0):
            x = x/i
            s = s + 1
        else:
            if s > 0:
                print(i,'^', s, sep = "", end = '')
                if x > 1 :
                    print(' * ', end = '')
            i = i + 1
            s = 0
            if(x == 1):
                print()
                break

