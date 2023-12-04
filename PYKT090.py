with open("CONTACT.in", "r") as f:
    res = []
    for i in f:
        i = i.lower().strip()
        if i not in res:
            res.append(i)
res.sort()
for i in res:
    print(i)