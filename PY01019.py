
for t in range(int(input())):
    check = 1
    s = input()
    ss = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(ss[i]) - ord(ss[i-1])):
            print("NO")
            check = 0
            break
    if check == 1:
        print("YES")