cnt = [0] * 10
def solve(n, flag):
    while n > 0:
        mod = n % 10
        n //= 10
        for i in range(1, mod + 1):
            cnt[i] += flag
        m = n
        while m > 0:
            cnt[m % 10] += (mod + 1) * flag
            m //= 10
        for i in range(10):
            cnt[i] += n * flag
        flag *= 10
        n -= 1


for _ in range(int(input())):
    cnt = [0]*10
    a, b = [int(i) for i in input().split()]
    solve(b, 1)
    solve(a - 1, -1)
    print(*cnt)

# 3
# 1 9
# 10 456
# 123 2437