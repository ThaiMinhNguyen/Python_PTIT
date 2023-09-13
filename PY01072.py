n, k = [int(x) for x  in input().split()]
l = map(int, input().split())
s = []
for i in l:
    if i not in s:
        s.append(i)

s.sort()
n = len(s)
a = []

def Try(id):
    if len(a) == k:
        for i in a:
            print(i, end = ' ')
        print()
    for j in range(id,n):
        a.append(s[j])
        Try(j+1)
        a.pop()

Try(0)

