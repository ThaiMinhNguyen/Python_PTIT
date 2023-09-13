import math
def isPrime(n):
    for i in range(2, int(math.sqrt(int(n)))+1):
        if n % i == 0:
            return False
    return n > 1

for t in range(int(input())):
    x = input()
    if(isPrime(int(x[-4:]))) :
        print("YES")
    else:
        print("NO")