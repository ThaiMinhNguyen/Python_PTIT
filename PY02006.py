for t in range(int(input())):
    n = int(input())
    a = list(map(int , input().split()))
    b = list(map(int , input().split()))
    a.sort()
    b.sort()
    check = 1
    for i,j in zip(a, b):
        if i > j:
            check = 0
            break
    if check == 1:
        print("YES")
    else:
        print("NO")