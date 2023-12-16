n = int(input())
ls = []
theloai = []
for _ in range(n):
    ls.append(len(input().split()))
i = 0
while i < n:
    if i < n and ls[i] == 7:
        # so_bai += 1
        theloai.append(2)
        i += 4
    if i < n and ls[i] == 6:
        # so_bai += 1
        theloai.append(1)
        while i < n and ls[i] == 6:
            i+=2
print(len(theloai), *theloai, sep='\n')


