for _ in range(int(input())):
    print("Test {:d}: ".format(_+1), end="")
    s1 = list(input())
    s2 = list(input())
    s1.sort()
    s2.sort()
    if(s1 == s2):
        print("YES")
    else:
        print("NO")