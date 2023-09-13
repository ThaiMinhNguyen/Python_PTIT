x = input()
s = ""
c = 0
# print(s)
for i in range(len(x)-1,-1,-1):
    c = c + 1
    s = s + x[i]
    if(c == 3 and i != 0):
        s = s + ','
        c = 0
print(s[::-1])