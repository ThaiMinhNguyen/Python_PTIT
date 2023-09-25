with open("A.txt") as f:
    a = f.read()
    print(a.count(input()))
