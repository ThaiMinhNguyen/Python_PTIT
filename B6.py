a, b = map(int, input().split())
mn = 20000
mx = 0
x = []
matrix = []
for i in range(a):
    y = list(map(int, input().split()))
    matrix.append(y)
    x.extend(y)
mn = min(x)
mx = max(x)
res = mx - mn
if res in x:
    print(res)
    for i in range(a):
        for j in range(b):
            if matrix[i][j] == res:
                print("Vi tri", '[{0}][{1}]'.format(i, j))
else:
    print("NOT FOUND")

