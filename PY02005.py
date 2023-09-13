n = int(input())
a = list(map(int, input().split()))
sum = 0
for i in range(0, n-1):
    for j in range(i+1, n):
        if a[i] > a[j]:
            sum = sum + 1
print(sum)