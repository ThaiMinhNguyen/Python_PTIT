a, b = map(int, input().split())
x = set(map(int, input().split()))
y = set(map(int, input().split()))
x = sorted(x)
y = sorted(y)
if len(x) != len(y):
    print("NO")
else:
    if x == y:
        print("YES")
    else:
        print("NO")
