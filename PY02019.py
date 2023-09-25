import math

n = int(input())
a = list(map(int, input().split()))
# a = set(a)
# a = sorted(a)
a.sort()
b = []
for i in range(0, len(a) - 1):
    for j in range(i+1, len(a)):
        if math.gcd(a[i], a[j]) == 1:
            print(a[i], a[j])
            b.append((a[i], a[j]))
b.sort()
# for i in b:
#     print(str(i[0]) + " " + str(i[1]))