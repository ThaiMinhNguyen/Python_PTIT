l1 =list(l.strip() for l in open("A.txt", "r"))
l2 =list(l.strip() for l in open("A.txt", "r"))
for i in range(len(l1)):
    try:
        print(int(l1[i]) * int(l2[i]))
    except:
        continue