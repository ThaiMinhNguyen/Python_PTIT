class Khach:
    def __init__(self, ma, ten, cu, moi):
        self.ma = "KH" + '%02d'%ma
        self.ten = ten
        self.cu = cu
        self.moi = moi
        self.sodien = moi - cu
        if self.sodien < 50:
            self.tong = 1.02*(100*self.sodien)
        elif self.sodien <= 100:
            self.tong = 1.03*(100*50 + 150*(self.sodien - 50))
        else:
            self.tong = 1.05 * (100 * 50 + 50 * 150 + 200 * (self.sodien - 100))

    def __str__(self):
        return f"{self.ma} {self.ten} {round(self.tong)}"

l = []
for i in range(int(input())):
    l.append(Khach(i + 1, input(), int(input()), int(input())))
l.sort(key=lambda x: -x.tong)
for i in l:
    print(i)