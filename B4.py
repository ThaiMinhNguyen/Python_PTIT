def Try(n, k):
    s = pow(2, n-1)
    if(k == s):
        return (chr)(ord('A') + n - 1)
    if(k > s):
       k -= s
    return Try(n-1, k)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(Try(a,b))