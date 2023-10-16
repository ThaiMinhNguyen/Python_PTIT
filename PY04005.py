import math


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def distance(self, x):
        return math.sqrt((self.a - x.a)*(self.a - x.a) + (self.b - x.b)*(self.b - x.b))

class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        c1 = self.x.distance(self.y)
        c2 = self.x.distance(self.z)
        c3 = self.y.distance(self.z)
        if c1 + c2 <= c3 or c1 + c3 <= c2 or c3 + c2 <= c1:
            return "INVALID"
        else:
            return "{:.3f}".format(c1 + c2 + c3)


t = int(input())
s = list(map(float, input().split()))
for _ in range(t-1):
    s.extend(list(map(float, input().split())))
for _ in range(t):
    k = Triangle(Point(s[0], s[1]), Point(s[2], s[3]), Point(s[4], s[5]))
    print(k)
    s = s[6:]


# 3
# 0 0 0 5 0 199
# 1 1 1 1 1 1
# 0 0 0 5 5 0