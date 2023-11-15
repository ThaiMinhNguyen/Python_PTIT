input()
a = list(set(list(map(int, input().split()))))
b = list(set(list(map(int, input().split()))))
check = 1
if len(a) != len(b):
    check = 0
else:
    i = 0
    while i < len(a):
        if a[i] == b[i]:
            i+=1
        else:
            check = 0
            break
if check:
    print("YES")
else:
    print("NO")
