for t in range(int(input())):
    x = input()
    sum = 0
    for i in x:
        sum = sum + int(i)
    sum = str(sum)
    if sum == sum[::-1] and len(sum) > 1:
        print("YES")
    else :
        print("NO")