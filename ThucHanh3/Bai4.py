from collections import deque

n = int(input())
s = deque()
s.append([int(input()), 1])
res = 0
for i in range(1, n):
    x = int(input())
    while len(s) > 0:
        if x < s[-1][0]:
            res += 1
            s.append([x, 1])
            break
        else:
            a = s.pop()
            res += a[1]
            if a[0] == x:
                if len(s) > 0:
                    res+=1
                s.append([x, a[1] + 1])
                break
    if len(s) == 0:
        s.append([x, 1])
print(res)

# 7
# 2
# 4
# 1
# 2
# 2
# 5
# 1