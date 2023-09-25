
file = open("CATHI.in", "r")
b = []
for t in range(int(file.readline())):
    a = []
    ma = "C" + '%03d'%(t+1)
    a.append(ma)
    ngay = file.readline()
    a.append(ngay.strip())
    gio = file.readline()
    a.append(gio.strip())
    id_thi = file.readline()
    a.append(id_thi.strip())
    b.append(a)
b1 = sorted(b, key = lambda x: (x[1], x[2], x[0]))
for i in b1:
    for k in i:
        print(k, end=" ")
    print()

