class HoaDon:
    def __init__(self, ma, ten, soluong, gia, ck):
        self.ck = ck
        self.gia = gia
        self.soluong = soluong
        self.ten = ten
        self.ma = ma
        self.tong = soluong * gia - ck

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.ma, self.ten, self.soluong, self.gia, self.ck, self.tong)


res = []
for _ in range(int(input())):
    res.append(HoaDon(input(), input(), int(input()),  int(input()),  int(input())))
res.sort(key=lambda x: -x.tong)
for i in res:
    print(i)
