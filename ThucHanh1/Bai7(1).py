def cont_pivot(a):
    cnt = 0
    max_left = a[0]
    for i in range(len(a)):
        pivot = a[i]
        max_left = max(max_left,a[i])
        right = a[i+1:]
        if pivot >= max_left and all(e > pivot for e in right):
            cnt+=1
    return cnt

for t in range(int(input())):
    cnt = 0
    n = int(input())
    a = list(map(int, input().split()))
    print(cont_pivot(a))

# 3
# 3
# 1 1 1
# 3
# 1 2 3
# 7
# 2 1 3 4 6 5 7