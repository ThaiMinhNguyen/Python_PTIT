class SinhVien:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.diem = 10

ls = []
t = int(input())
for _ in range(t):
    ls.append(SinhVien(input(), input(), input()))

for _ in range(t):
    ma, cc = map(str, input().split())
    tru = 0
    for i in cc:
        if i == 'm':
            tru += 1
        elif i == 'v':
            tru+= 2
    for i in ls:
        if ma == i.ma:
            i.diem -= tru
            if(i.diem < 0): i.diem = 0
            break
for i in ls:
    print(i.ma, i.ten, i.lop, i.diem, end = " ")
    if(i.diem == 0):
        print("KDDK")
    else:
        print()
