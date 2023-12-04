
def Try(i):
    global s, used, n
    if i > n:
        res.append(''.join(s[1:n+1]))
    for j in range(1, n+1):
        if used[j] == False:
            used[j] = True
            s[i] = str(j)
            Try(i+1)
            used[j] = 0


for _ in range(int(input())):
    n = int(input())
    s = [0]*(n+4)
    used = [False] * (n+1)
    res = []
    Try(1)
    res.reverse()
    print(len(res))
    print(*res)