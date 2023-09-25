import math
# def find_largest(a, b):
#     m = float("inf")
#     p = []
#     i = 2
#     while i * i <= b:
#         if b % i == 0:
#             p.append(i)
#             b //= i
#         else:
#             i += 1
#     if b > 1:
#         p.append(b)
#     for i in set(p):
#         cnt = 0
#         t = a
#         while t >= i:
#             cnt += t//i
#             t //= i
#         m = min(m, cnt)
#     if m == float("inf"):
#         return 0
#     else:
#         return m

for t in range(int(input())):
    a, b = map(int, input().split())
    res = 0
    s = math.factorial(a)
    while(s % b == 0):
        s //= b
        res += 1
    print(res)

