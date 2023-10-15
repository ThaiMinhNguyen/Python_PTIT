import math

a, b = map(int, input().split())
l = math.gcd(a,b)
print(int(a/l), '/', int(b/l), sep="")