for t in range(int(input())):
    x = input()
    y = x[::-1]
    check = 1
    for i in range(1,len(x)):
        if(abs(ord(x[i]) - ord(x[i-1])) != abs(ord(y[i]) - ord(y[i-1]))):
            check = 0
            break
    if check == 0 :
        print("NO")
    else:
        print("YES")