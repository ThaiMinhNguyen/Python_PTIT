f1 = open("SOTAY.txt", "r")
f2 = open("DIENTHOAI.txt", "w")
s = f1.readlines()
i = 0
res = []
while i < len(s):
    k = s[i].strip().split()
    if k[0] == "Ngay":
        ngay = k[1]
        i+=1
        hoten = s[i].strip().split()
        i+=1
        sdt = s[i].strip()
        i+=1
        ho = hoten[0]
        ten = hoten[-1]
        ten_dem = ' '.join(hoten[1:-1])
        res.append([ho, ten_dem, ten, sdt, ngay])
    else:
        hoten = s[i].strip().split()
        i += 1
        sdt = s[i].strip()
        i += 1
        ho = hoten[0]
        ten = hoten[-1]
        ten_dem = ' '.join(hoten[1:-1])
        res.append([ho, ten_dem, ten, sdt, ngay])
res.sort(key=lambda x:(x[2], x[1]))
for i in res:
    f2.write("{} {} {}: {} {}\n".format(i[0], i[1], i[2], i[3], i[4]))
# f1.close()
# f2.close()
# print(s)