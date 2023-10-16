class HocSinh:
    def __init__(self, ma, ten, s):
        self.ma = "HS" + '%02d'%ma
        self.ten = ten
        self.diem = round((sum(s) + s[0] + s[1])/(len(s)+2) + 0.01, 1)
        if self.diem >= 9:
            self.status = "XUAT SAC"
        elif self.diem >= 8:
            self.status = "GIOI"
        elif self.diem >= 7:
            self.status = "KHA"
        elif self.diem >= 5:
            self.status = "TB"
        else:
            self.status = "YEU"

    def __str__(self):
        return f"{self.ma} {self.ten} " + str(self.diem) + " " + self.status

l = []
for cnt in range(int(input())):
    ten = input()
    s = list(map(float, input().split()))
    l.append(HocSinh(cnt+1, ten, s))
l.sort(key=lambda x: [-x.diem, x.ma])
for i in l:
    print(i)


