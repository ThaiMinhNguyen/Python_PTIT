def isValid(s):
    if len(s) % 2 == 1 or s != s[::-1]:
        return False
    for i in s:
        if(int(i) % 2 == 1):
            return False
    return True

for t in range(int(input())):
    x = int(input())
    for i in range(22, x, 1):
        if isValid(str(i)):
            print(i, end = " ")
    print()