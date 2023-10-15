ls = list()
a = open("SOTAY.txt", 'r')
b = open("DIENTHOAI.txt", 'w')
l = a.readlines()
i = 0
while i < len(l):
    k = list(l[i].strip().split())
    if k[0] == "Ngay":
        i += 1
        ngay = k[1]
        # print(ngay)
        hoten = list(l[i].strip().split())
        ten = hoten[-1]
        ten_dem = ' '.join(hoten[0:-1])
        i+=1
        sdt = l[i].strip()
        i+=1
        ls.append([ngay, ' '.join(hoten), sdt, ten, ten_dem])
    else:
        hoten = list(l[i].strip().split())
        ten = hoten[-1]
        ten_dem = hoten[1:-1]
        i += 1
        sdt = l[i].strip()
        i += 1
        ls.append([ngay, ' '.join(hoten), sdt, ten, ten_dem])
ls = sorted(ls, key= lambda x: (x[3], x[4]))
for i in ls:
    st = i[1] + ': ' + i[2] + ' ' + i[0]
    b.write(st)
    b.write('\n')
    # print(st)
