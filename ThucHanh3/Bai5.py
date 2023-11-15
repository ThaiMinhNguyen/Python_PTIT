n, k = map(int, input().split())
prev = list(map(int, input().split()))
aft = list(map(int, input().split()))
a = []
s = 0
for i in range(n):
    a.append([prev[i], aft[i]])
a.sort(key=lambda x: x[0] - x[1])
for i in range(k):
    s += a[i][0]
for l in range(k, n):
    s += min(a[l][0], a[l][1])


print(s)

# 3 1
# 5 4 6
# 3 1 5

# 5 4
# 3 4 7 10 3
# 4 5 5 12 5