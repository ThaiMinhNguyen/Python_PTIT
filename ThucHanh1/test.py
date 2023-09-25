b = 100
p = []
i = 2
while i * i <= b:
    if b % i == 0:
        p.append(i)
        b //= i
    else:
        i += 1
if b > 1:
    p.append(b)
print(p)