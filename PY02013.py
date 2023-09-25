
while(True):
    sum = 1
    x = int(input())
    if(x == 0):
        break
    while(x != 1):
        while(x % 2 == 0):
            x = x / 2
            sum = sum + 1
        while(x % 2 != 0 and x != 1):
            x = x * 3 + 1
            sum = sum+ 1
    if(x == 1):
        print(sum)

