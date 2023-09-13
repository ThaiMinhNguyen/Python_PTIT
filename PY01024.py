def check(n):
    sum = 0
    c = 1
    for i in range(0, len(n)):
        sum += int(n[i])
        if(abs(int(n[i]) - int(n[i-1])) != 2):
            print("NO")
            c = 0
            break
    if c == 1 :
        if sum % 10 == 0 :
            print("YES")
        else:
            print("NO")


for t in range(int(input())):
    x = input()
    check(x)




