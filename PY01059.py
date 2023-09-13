for t in range(int(input())):
    x = input()
    sum = 0
    mul = 0
    check = 1
    for i in range(len(x)):
        if(i % 2 == 0):
            sum = sum + int(x[i])
        else:
            if(int(x[i]) != 0):
                if mul == 0:
                    mul = int(x[i])
                else:
                    mul = mul * int(x[i])
    print(str(sum) + ' ' + str(mul))
