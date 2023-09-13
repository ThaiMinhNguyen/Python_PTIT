a = [0] * 93
a[1]= a[2] = 1

for i in range(3, 93):
    a[i] = a[i-1] + a[i-2]

for t in range(int(input())):
    x, y = (int(x) for x in input().split());
    for i in range(x, y+1):
        print(a[i], end = " ")
    print()