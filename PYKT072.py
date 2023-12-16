n = int(input())
ls = []
ls.append(input())
l = len(ls[0])
c = 1
for _ in range(n-1):
    x = input()
    ls.append(x)
    if l != len(x):
        c = 0
if c == 0:
    print("-1")
else:
    # print(l)
    res = l * n
    check = ls[0]
    for i in range(l):
        r = 0
        check = check[1:l] + check[0]
        # print("Check la", check)
        for j in range(0, n):
            c = 0
            crt = ls[j]
            if crt == check:
                c = 1
                # print("Ko xoay", end = "")
                continue
            for k in range(l-1):
                crt = crt[1:l] + crt[0]
                # print(crt , end= ' ')
                if crt == check:
                    c = 1
                    r += k+1
                    break
            if c == 0:
                break
            # print()
        res = min(res, r)
    if c == 0:
        print(-1)
    else:
        print(res)


