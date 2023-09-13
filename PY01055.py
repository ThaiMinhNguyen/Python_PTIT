for t in range(int(input())):
    x = input()
    if len(x) % 2 != 0:
        if x[0] != x[1]:
            check = 1
            for i in range(2, len(x), 2):
                if x[i] != x[i-2]:
                    check = 0
                    break
            if check == 0 :
                print('NO')
            else:
                print("YES")
        else:
            print('NO')
    else:
        print("NO")