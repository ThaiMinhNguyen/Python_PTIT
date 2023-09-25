def chuanhoa(ten):
    ds_tu = ten.lower().strip().split()
    ds_tu_chuan = [t.capitalize() for t in ds_tu]
    ho_ten = ' '.join(ds_tu_chuan)
    return ho_ten


ds = []
for t in range(int(input())):
    ma = "TS{:02d}".format(t+1)
    ten = chuanhoa(input())
    diemthi = float(input())
    dan_toc = input()
    khu_vuc = int(input())
    diem = diemthi
    if(dan_toc != "Kinh"):
        diem += 1.5
    if(khu_vuc == 1):
        diem += 1.5
    elif khu_vuc == 2:
        diem += 1
    ds.append([ma, ten, diem])

ds.sort(key=lambda x: (-x[2], x[0]))
dien_chuan = 20.5  # Điểm chuẩn
for i, thong_tin in enumerate(ds):
    ma, ten, diem = thong_tin[0], thong_tin[1], thong_tin[2]
    trang_thai = "Do" if diem >= dien_chuan else "Truot"
    print(f"{ma} {ten} {diem:.1f} {trang_thai}")


# 2
# Nguyen  hong ngat
# 22
# Kinh
# 1
#   Chu thi MINh
# 14
# Dao
# 3