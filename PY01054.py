for t in range(int(input())):
    x = input()
    sum = 1
    for i in x:
        if(int(i) != 0):
            sum = sum * int(i)
    print(sum)