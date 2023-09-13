for t in range(int(input())):
    s = input()
    x = len(s)
    if s[x-2] == '8' and s[x-1] == '6':
        print("YES")
    else:
        print("NO")
