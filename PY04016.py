from datetime import datetime

class Khach:
    def __init__(self, ma, ten, sophong, ngaynhan, ngaytra, dichvu):
        self.ma = "KH{:02d}".format(ma)
        self.ten = ten
        self.sophong = sophong
        # self.ngaynhan = ngaynhan
        # self.ngaytra = ngaytra
        date_format = "%d/%m/%Y"
        d0 = datetime.strptime(ngaynhan, date_format)
        d1 = datetime.strptime(ngaytra, date_format)
        d = d1 - d0
        self.sonngayo = d.days + 1
        # self.dichvu = dichvu
        if sophong[0] == '1':
            self.tong = self.sonngayo * 25 + dichvu
        elif sophong[0] == '2':
            self.tong = self.sonngayo * 34 + dichvu
        elif sophong[0] == '3':
            self.tong = self.sonngayo * 50 + dichvu
        elif sophong[0] == '4':
            self.tong = self.sonngayo * 80 + dichvu

    def __str__(self):
        return "{} {} {} {} {}".format(self.ma, self.ten, self.sophong, self.sonngayo, self.tong)

if __name__ == "__main__":
    res = []
    for _ in range(int(input())):
        res.append(Khach( _ + 1, input().strip(), input().strip(), input().strip(), input().strip(), int(input())))
    res.sort(key=lambda x: x.tong, reverse=True)
    for i in res:
        print(i)
