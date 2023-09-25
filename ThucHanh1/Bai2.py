file = open("CONTACT.in", "r")
a = list(s.strip() for s in file.readlines())
b = []
for i in range(len(a)):
    b.append(a[i].lower())
for i in sorted(set(b)):
    print(i)