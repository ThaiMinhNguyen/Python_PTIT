tl = {}
n, m  = map(int, input().split())
for i in range(n):
    s = "TL{:03d}".format(i+1)
    t = input()
    tl[s] = t
res = []
for i in range(m):
    ma = "P{:03d}".format(i+1)
    t = input()
    theloai = tl[t]
    ngay, thang, nam = map(int, input().split('/'))
    ten = input()
    tap = int(input())
    res.append([ma, theloai, ngay, thang, nam, ten, tap])
# res = sorted(res.sort(key=lambda x: (-x[2], -x[3], -x[4])), key=lambda x: x[5])
# res = sorted(res, key=lambda x : x[6])
res = sorted(sorted(sorted(res, key=lambda x: -x[6]), key=lambda x : x[5]), key=lambda x: (x[4], x[3], x[2]))
for x in res:
    print("{} {} {:02d}/{:02d}/{} {} {}".format(x[0], x[1], x[2], x[3], x[4], x[5], x[6]))

# 2 3
# Hai huoc
# Tinh cam
# TL001
# 25/11/2021
# Phim so 1
# 10
# TL001
# 04/12/2021
# Phim so 2
# 15
# TL002
# 25/11/2021
# Phim so 3
# 5

