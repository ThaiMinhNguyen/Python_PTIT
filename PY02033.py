s = input()
n = len(s)
if n % 2 != 0:
    n-=1
a = []
for i in range(0, n, 2):
    k = int(s[i:i+2])
    if k not in a:
        a.append(k)
print(*a)