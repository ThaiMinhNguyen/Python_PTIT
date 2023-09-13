for t in range(int(input())):
    x = input()
    if(x[0] == x[len(x)-2] and x[1] == x[len(x)-1]):
        print("YES")
    else:
        print("NO")

