for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    c = 1
    for i in range(n):
        if a[i] > b[i]:
            print('NO')
            c = 0
            break
    if c == 1:
        print("YES")
