class GV:
    def __init__(self, id, ten, ma, d1, d2):
        self.id = "GV{:02d}".format(id)
        self.ten = ten
        self.ma = ma
        self.d1 = d1
        self.d2 = d2
        self.tong = d1 * 2 + d2
        if ma[1] == '1':
            self.tong += 2
        elif ma[1] == '2':
            self.tong += 1.5
        elif ma[1] == '3':
            self.tong += 1

        if ma[0] == 'A':
            self.mon = "TOAN"
        elif ma[0] == 'B':
            self.mon = "LY"
        elif ma[0] == 'C':
            self.mon = "HOA"

        if self.tong >= 18:
            self.status = "TRUNG TUYEN"
        else:
            self.status = "LOAI"

    def __str__(self):
        return "{} {} {} {:.1f} {}".format(self.id, self.ten, self.mon, self.tong, self.status)

res = []
for _ in range(int(input())):
    res.append(GV(_ + 1, input(), input(), float(input()), float(input())))
res.sort(key=lambda x: -x.tong)
for i in res:
    print(i)
