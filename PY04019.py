class NhanVien:
    def __init__(self, ma, ten, tong):
        self.ma = ma
        self.ten = ten
        # if d1 > 10:
        #     d1/=10
        # if d2 > 10:
        #     d2/=10
        self.tong = tong
    def getStatus(self):
        if self.tong > 9.5:
            return 'XUAT SAC'
        if self.tong >= 8:
            return 'DAT'
        if self.tong >= 5:
            return 'CAN NHAC'
        return 'TRUOT'

    def __str__(self):
        return '{} {} {:.2f} {}'.format(self.ma, self.ten, self.tong, self.getStatus())


l = []
for i in range(int(input())):
    ma = "TS0{}".format(i+1)
    ten = input()
    d1 = float(input())
    d2 = float(input())
    if d1 > 10:
        d1 /= 10
    if d2 > 10:
        d2 /= 10
    l.append(NhanVien(ma, ten, (d1+d2)/2))

l.sort(key=lambda x: -x.tong)
for i in l:
    print(i)

# 3
# Nguyen Thai Binh
# 45
# 75
# Le Cong Hoa
# 4
# 4.5
# Phan Van Duc
# 56
# 56