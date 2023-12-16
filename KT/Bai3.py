for _ in range(int(input())):
    n = int(input())
    res = []
    for i in range(n):
        a, b = map(int, input().split())
        res.append([a,b])
    res.sort(key=lambda x: x[0])