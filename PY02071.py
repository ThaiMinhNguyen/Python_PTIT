
n, v, x = 0, [], []

def Try(k) :
    p = n - k
    if len(x) and x[-1] < p :
        p = x[-1]
    for i in range(p, 0, -1) :
        x.append(i)
        if i + k == n :
            # print(*x)
            v.append(x[:])
        else :
            Try(k + i)
        x.pop()

t = int(input())
for i in range(t) :
    x, v = [], []
    n = int(input())
    Try(0)
    print(len(v))
    for j in v :
        print('(', j[0], sep = '', end = '')
        for k in range(1, len(j)) :
            print(' ', j[k], sep = '', end = '')
        print(')', end = ' ')
    print()
