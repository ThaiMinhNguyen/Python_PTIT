x = input()
lc = sum(1 for c in x if c.islower())
uc = sum(1 for c in x if c.isupper())

if lc >= uc :
    print(x.lower())
else:
    print(x.upper())