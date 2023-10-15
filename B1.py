for _ in range(int(input())):
    a = input()
    c = 1
    s = list(map(int, input().split()))
    for i in range(0, len(s) -1):
        if s[i] == s[i+1]:
            c = 0
            break
    if c == 1:
        print("YES")
    else:
        print("NO")
