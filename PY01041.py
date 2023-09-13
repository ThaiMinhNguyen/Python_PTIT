for i in range(int(input())) :
    x = input();
    if len(x) >= 3 :
        check = 1
        for i in range(0, len(x) - 1):
            if(int(x[i]) >= int(x[i+1])) :
                p = i
                break
        # print(x[p])
        if(int(x[p]) == int(x[p+1])):
            check = 0
        else :
            for i in range(p+1, len(x) - 1):
                if(int(x[i]) <= int(x[i+1])):
                    check = 0
                    break
        if check == 0:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")


