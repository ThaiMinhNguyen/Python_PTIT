for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    b = {}
    for i in a:
        if i not in b.keys():
            b[i] = 1
        else:
            b[i] += 1
    for k,v in b.items():
        if(v % 2 != 0):
            print(k)

# 2
# 7
# 1 2 3 2 3 1 3
# 5
# 1 1 3 3 2