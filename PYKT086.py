f = '0123456789ABCDEF'
def doi(n, k):
    s = ''
    while (n > 0):
        x = n % k
        s = f[x] + s
        n //= k
    print(s)
f1 = open("DATA.in", "r")
n = int(f1.readline())
for _ in range(n):
    a = int(f1.readline())
    b = int(f1.readline(),2)
    doi(b, a)


# s = '0123456789ABCDEF'
# with open('DATA.in', 'r') as f:
#     t = int(f.readline())
#     for __ in range(t):
#         n = int(f.readline())
#         num = int(f.readline(), 2)
#         res = ''
#         while num:
#             res += s[num%n]
#             num //= n
#         print(res[::-1])