for t in range(int(input())):
    x = input()
    sum = 0
    for i in x:
        sum = sum + int(i)
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")