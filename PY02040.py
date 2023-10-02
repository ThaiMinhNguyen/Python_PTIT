a = []
t = int(input())
s = 0
for _ in range(t):
    b = list(map(int, input().split()))
    s += sum(b)
    a.append(b)
k = int(input())
res = 0
cheo = 0
c = t - 1
for i in range(t):
    for j in range(0, c):
        if(j != c):
            res += a[i][j]
    cheo += a[i][c]
    c-=1

if abs(res - (s - cheo - res)) <= k:
    print("YES")
else:
    print("NO")
print (abs(res- (s - cheo - res)))