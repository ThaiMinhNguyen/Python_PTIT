import math
def isPrime(n):
    for i in range(2, int(math.sqrt(int(n)))+1):
        if n % i == 0:
            return False
    return n > 1

for t in range(int(input())):
    x = input()
    check = 1
    for i in range(len(x)):
        if (isPrime(i) == False and isPrime(int(x[i])) == True) or (isPrime(i) == True and isPrime(int(x[i])) == False):
            print("NO")
            check = 0
            break
    if check == 1:
        print("YES")