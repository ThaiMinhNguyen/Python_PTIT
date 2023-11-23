s = input()
# n = int(len(s)/2)
# print(s[0:n], s[n:])
while len(s) > 1:
    n = int(len(s)/2)
    i = int(s[0:n]) + int(s[n:])
    s = str(i)
    print(s)
