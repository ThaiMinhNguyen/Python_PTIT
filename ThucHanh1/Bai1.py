n = int(input())
a = list(map(int, input().split()))
b = []
a.sort()
b.append(a[0]*a[1]*a[2])
b.append(a[0]*a[1])
b.append(a[n-1]*a[n-2])
b.append(a[n-1]*a[n-2]*a[n-3])
b.append(a[0]*a[1]*a[n-1])
print(max(b))


