s = input()
j = int(input())
n = len(s)
if n % 2 != 0:
    n-=1
a = []
b = {}
for i in range(0, n, 2):
    k = int(s[i:i+2])
    if k not in a:
        b[k] = 1
        a.append(k)
    else:
        b[k] += 1
a.sort()
c = 0
# print(j)
for i in a:
    if b[i] >= j:
        c = 1
        print(i , b[i])
if c == 0:
    print("NOT FOUND")