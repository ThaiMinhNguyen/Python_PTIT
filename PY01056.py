import math
def isPrime(n):
    for i in range(2, int(math.sqrt(int(n)))+1):
        if n % i == 0:
            return False
    return n > 1

for t in range(int(input())):
    x = input()
    check = 1
    sum = 0
    for i in range(0, len(x)):
        if(i % 2 == 0):
            if int(x[i]) % 2 != 0:
                check = 0
                break
        if (i % 2 != 0):
            if int(x[i]) % 2 == 0:
                check = 0
                break
        sum = sum + int(x[i])
    if(check == 0 or isPrime(sum) == False):
        print("NO")
    else:
        print("YES")