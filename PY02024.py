def tinhtong(s):
    s = str(s)
    sum = 1
    for i in range(len(s)):
        sum *= int(s[i])
    return sum

# print(tinhtong(123))
for t in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    b = {}
    for i in a:
        b[i] = tinhtong(i)
    c = dict(sorted(b.items(), key= lambda x:(x[1], x[0])))
    for i in c.keys():
        print(i, end = " ")
    print()
