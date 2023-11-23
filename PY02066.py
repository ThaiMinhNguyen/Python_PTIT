n = int(input())
a = []
while len(a) < n:
    b = list(map(int, input().split()))
    a += b
a.sort()
if n == a[-1]:
    print("Excellent!")
else:
    j = 0
    for i in range(1, a[-1]+1):
        if a[j] == i:
            j+=1
        else:
            print(i)

