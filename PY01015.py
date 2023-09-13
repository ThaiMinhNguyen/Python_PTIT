def check(n):
    temp = 1
    for i in n:
        if int(i) < temp:
            return False
        else:
            temp = int(i)
    return True

for t in range(int(input())):
    x = input()
    if check(x):
        print("YES")
    else:
        print("NO")
