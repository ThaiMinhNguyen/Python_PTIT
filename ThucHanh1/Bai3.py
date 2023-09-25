def doi(a, base):
    mstring = ''
    if a == 0:
        return "0"
    while a:
        mstring += str(a%base)
        a//=base
    return mstring[::-1]

a, b, m = map(int, input().split())
sum = 0
for i in range(a, b+1):
    s = doi(i, m)
    if(s == s[::-1]):
        sum += 1
        print(s)
print(sum)