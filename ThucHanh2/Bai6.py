a, b = map(int, input().split())
ar = list(map(int, input().split()))
sl = a-1
ok = 0
dau = [""] * sl
pheptinh = ["+", "-", "*"]

def check():
    global ok
    s = ""
    if (ar[0] < 0):
        s += '(' + str(ar[0]) + ')'
    else:
        s += str(ar[0])
    for i in range(0, sl):
        s += dau[i]
        if(ar[i+1] < 0):
            s += '(' + str(ar[i+1]) +')'
        else:
            s += str(ar[i+1])

    if eval(s) == b:
        ok = 1
        s += '=' + str(b)
        print(s)

def Try(i):
    for j in pheptinh:
        dau[i] = j
        if i == sl - 1: check()
        else: Try(i+1)

Try(0)
if not ok :
    print("IMPOSSIBLE")

# 5 20
# 1 2 3 4 5