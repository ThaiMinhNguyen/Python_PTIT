for t in range(int(input())):
    x = input()
    sum = 0
    mul = 1
    check = 1
    for i in range(len(x)):
        if(i % 2 == 0 and x[i] != '0'):
            mul = mul * int(x[i])
        else:
            sum = sum + int(x[i])
    print(str(mul) + ' ' + str(sum))
