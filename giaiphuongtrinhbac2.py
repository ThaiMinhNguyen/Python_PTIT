import math
a, b, c = map(int, input().split());
delta =  b*b - 4*a*c
if delta < 0:
    print("Vo Nghiem")
elif delta == 0:
    x = -b/(2*a)
    print(x)
else:
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    print(x1)
    print(x2)

