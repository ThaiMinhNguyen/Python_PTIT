ds = {}
for _ in range(int(input())):
    s = input().split()
    ngay = s[4]
    if ngay not in ds:
        ds[ngay] = 0
    if s[3] == "IN":
        if s[1] == "Xe_con":
            if int(s[2]) == 5:
                ds[ngay] += 10000
            else:
                ds[ngay] += 15000   
        elif s[1] == "Xe_khach":
            if int(s[2]) == 29:
                ds[ngay] += 50000
            else:
                ds[ngay] += 70000
        else:
            ds[ngay] += 20000
ds = dict(sorted(ds.items(), key=lambda x:x[0]))
for k, v in ds.items():
    print("{}: {}".format(k,v))