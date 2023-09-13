import math
def isPrime(n):
    for i in range(2, int(math.sqrt(int(n)))+1):
        if n % i == 0:
            return False
    return n > 1

for t in range(int(input())):
    x = input()
    sum = 0
    if isPrime(len(x)) :
        for i in x:
            if isPrime(int(i)):
                sum = sum + 1
        if sum > len(x) - sum :
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


