# n = int(input())
# a = list(map(int, input().split()))
# b = [0] * n
# c = [1] * n
# b[0] = a[0]
# for i in range(1, n):
#     b[i] = a[i]
#     b[i] = max(b[i], (b[i-1] + b[i])/(c[i-1]+1))
#     if b[i] == (b[i-1] + a[i])/(c[i-1]+1):
#         c[i] = c[i-1] + 1
# res = 0
# k = max(b)
# print(*b)
# for i in range(n):
#     if k == b[i]:
#         res = max(res, c[i])
# print(res)


n = int(input()) + 1
a = [int(x) for x in input().split()] + [-1]
print(*a)
ans, x, k = 0, 0, max(a)
for i in range(n):
    if a[i] == k:
        x += 1
    else:
        ans = max(ans, x)
        x = 0
print(ans)

