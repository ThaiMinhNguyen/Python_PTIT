import cmath

for _ in range(int(input())):
    a = list(map(int, input().split()))
    x = complex(a[0], a[1])
    y = complex(a[2], a[3])
    z = (x+y)*x
    l = (x+y)**2
    print("{} + {}i, {} + {}i".format(int(z.real), int(z.imag), int(l.real), int(l.imag)))