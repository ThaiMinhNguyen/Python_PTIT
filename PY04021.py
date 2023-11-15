def change(s):
    k = list(map(int, s.split(':')))
    return k[0] * 60 + k[1]

class Gamer:
    def __init__(self, ma, ten, giovao, giora):
        self.ten = ten
        self.ma = ma
        self.tong = change(giora) - change(giovao)

    def __str__(self):
        return "{} {} {} gio {} phut".format(self.ma, self.ten, int(self.tong/60), self.tong - int(self.tong/60)*60)

l = []
for i in range(int(input())):
    l.append(Gamer(input(), input(), input(), input()))

l.sort(key=lambda x : -x.tong)
for i in l:
    print(i)
        
# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00
