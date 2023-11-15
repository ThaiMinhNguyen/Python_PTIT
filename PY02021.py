for _ in range(int(input())):
    a1, b1, c1 = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = []
    i, j, k = 0, 0, 0
    ok = 0
    while i < a1 and j < b1 and k < c1:
        if(a[i] == b[j] == c[k]):
            d.append(a[i])
            i += 1
            j += 1
            k += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[k]:
            j += 1
        else:
            k += 1
    if len(d):
        print(*d)
    else:
        print("NO")

# 3
# 6 5 8
# 1 5 10 20 40 80
# 5 7 20 80 100
# 3 4 15 20 30 70 80 120
# 3 5 4
# 1 5 5
# 3 4 5 5 10
# 5 5 10 20
# 3 3 3
# 1 2 3
# 4 5 6
# 7 8 9