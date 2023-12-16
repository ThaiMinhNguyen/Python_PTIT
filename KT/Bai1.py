for _ in range(int(input())):
    n = int(input())
    f = [0] * (n+3)
    x, y, z = map(int, input().split())
    f[1] = x
    for i in range(2, n+1):
        f[i] = min(f[i - 1] + x, f[i // 2] + z if i % 2 == 0 else f[(i + 1) // 2] + z + y)
    print(f[n])


