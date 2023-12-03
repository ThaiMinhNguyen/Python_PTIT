class ThiSinh:
    def __init__(self, ten, diadiem, gio):
        self.ma = ""
        diadiem_l = [i[0] for i in diadiem.split()]
        # for i in diadiem_l:
        #     self.ma += i[0]
        ten_l = [i[0] for i in ten.split()]
        # for i in ten_l:
        #     self.ma += i[0]
        self.ma = ''.join(diadiem_l) + ''.join(ten_l)
        self.ma.upper()
        tg = [int(i) for i in gio.split(':')]
        so_phut = tg[0] * 60 + tg[1] - 6 * 60
        self.tocdo = 120 / so_phut * 60
        self.diadiem = diadiem
        self.ten = ten

    def __str__(self):
        return "{} {} {} {} Km/h".format(self.ma, self.ten, self.diadiem, round(self.tocdo))

res = []
for _ in range(int(input())):
    res.append(ThiSinh(input().strip(), input().strip(), input().strip()))
res.sort(key=lambda x: -x.tocdo)
for i in res:
    print(i)

# 3
# Tran Vu Minh
# Ha Noi
# 8:30
# Vu Ngoc Hoang
# Hoa Binh
# 8:20
# Pham Dinh Tan
# An Giang
# 8:45