
def tinh_luong(luong_co_ban, so_ngay_cong, he_so_nhan):
    return int(luong_co_ban) * int(so_ngay_cong) * int(he_so_nhan)

he_so = {
    'A':[10, 12, 14, 20],
    'B':[10, 11, 13, 16],
    'C':[9, 10, 12, 14],
    'D':[8, 9, 11, 13]
}

p = {}
for t in range(int(input())):
    ds_tu = input().split()
    p[ds_tu[0]] = ' '.join(ds_tu[1:])

danh_sach_nv = []
for _ in range(int(input())):
    ma = input()
    ten = input()
    luongcoban = input()
    ngaycong = input()
    danh_sach_nv.append((ma, ten, luongcoban, ngaycong))

for nv in danh_sach_nv:
    ma, ten, luongcoban, ngaycong = nv
    if(int(ma[1:3]) <= 3):
        he_so_nhan = he_so[ma[0]][0]
    elif (int(ma[1:3]) <= 8):
        he_so_nhan = he_so[ma[0]][1]
    elif (int(ma[1:3]) <= 15):
        he_so_nhan = he_so[ma[0]][2]
    else:
        he_so_nhan = he_so[ma[0]][3]
    luong = tinh_luong(luongcoban, ngaycong, he_so_nhan)
    print(ma, " ", ten, " ", p[ma[3:5]], " ", luong*1000)




# 2
# HC Hanh chinh
# KH Ke hoach Dau tu
# 2
# C06HC
# Tran Binh Minh
# 65
# 25
# D03KH
# Le Hoa Binh
# 59
# 24