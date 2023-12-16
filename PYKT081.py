for _ in range(int(input())):
    c = 1
    x = input().split('.')
    if len(x) != 4:
        c = 0
    else:
        try:
            for i in x:
                if int(i) < 0 or int(i) > 255:
                    c = 0
                    break
        except:
            c = 0
    if c == 0:
        print("NO")
    else:
        print("YES")
    # print(x)
# 2
# 192.168.1.1
# 256.255.255.255