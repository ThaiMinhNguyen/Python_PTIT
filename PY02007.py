a = []
while len(a) < 10:
    a += list(int(x) % 42 for x in input().split())
a = set(a)
print(len(a))