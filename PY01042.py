for t in range(int(input())):
    x = input()
    check = 1
    for i in x:
        if(i != '0' and i != '1' and i != '2'):
            check = 0
            print("NO")
            break;
    if check == 1:
        print("YES")
