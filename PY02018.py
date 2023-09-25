n = int(input())
a = list(map(int, input().split()))
m = max(a)
for i in range(1,m + 2):
    if i not in a:
        print(i)
        break