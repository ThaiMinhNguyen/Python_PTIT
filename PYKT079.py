for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    res = []
    for i in ls:
        if i not in res:
            res.append(i)
    mn = min(res)
    mx = max(res)
    print(mx - mn + 1 - len(res))
