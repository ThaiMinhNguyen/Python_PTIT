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
for i in range(t):
    for j in range(i, t):
        if(i != j):
            res+= a[i][j]
        else:
            cheo += a[i][j]

if res- (s - cheo - res) <= k:
    print("YES")
else:
    print("NO")
print (abs(res- (s - cheo - res)))