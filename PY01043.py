for t in range(int(input())):
    n = int(input())
    for i in range(22, n):
        s = str(i)
        check = 1
        if(s == s[::-1]):
            if(len(s) % 2 == 0):
                for j in s:
                    if(j == '2' or j == '4' or j == '6' or j == '8' or j == '0'):
                        continue
                    else:
                        check = 0
                        break
                if check == 0:
                    continue
                else:
                    print(s, end = ' ')
        else:
            continue
    print()
