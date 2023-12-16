def doi(n):
    if n <= 4:
        return 2.5
    elif n <= 6:
        return 3
    elif n <= 9:
        return 3.5
    elif n <= 12:
        return 4
    elif n <= 15:
        return 4.5
    elif n <= 19:
        return 5
    elif n <= 22:
        return 5.5
    elif n <= 26:
        return 6
    elif n <= 29:
        return 6.5
    elif n <= 32:
        return 7
    elif n <= 34:
        return 7.5
    elif n <= 36:
        return 8
    elif n <= 38:
        return 8.5
    else:
        return 9

for _ in range(int(input())):
    a, b, c, d = map(float, input().split())
    a = doi(a)
    b = doi(b)
    diem = (a + b + c + d)/4
    if diem - int(diem) >= 0.25 and diem - int(diem) < 0.75:
        diem = int(diem) + 0.5
    elif diem - int(diem) >= 0.75:
        diem = int(diem) + 1
    else:
        diem = int(diem)
    print("{:.1f}".format(diem))

