def doi(n, m):
    res = ""
    while n:
        res += str(n % m)
        n //= m
    return res == res[::-1]

def check_bin(n):
    tmp = bin(n)[2:]
    return tmp == tmp[::-1]

a, b, m = map(int, input().split())
res = [i for i in range(a, b+1) if check_bin(i)]
for j in range(3, m+1):
    res = [i for i in res if doi(i, j)]
    if len(res) == 0:
        break
print(len(res))

