n = int(input())
a = []
sum = 0
a = list(int(x) for x in input().split())
# print(a)
for i in range(1, n):
    if(a[i] != a[i-1]):
        sum = sum + 1
print(sum)