
while True:
    res = []
    x = int(input())
    if x == 0:
        break
    for i in range(x):
        res.append(int(input()))
    # res.sort()
    mn = min(res)
    mx = max(res)
    if(mn != mx):
        print(mn, mx)
    else:
        print("BANG NHAU")
