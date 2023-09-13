import math

def isPrime(n):
    for i in range(2, int(math.sqrt(int(n)))+1):
        if n % i == 0:
            return False
    return n > 1

for t in range(int(input())):
    x, y = map(int, input().split())
    z = math.gcd(x, y)
    # print(z)
    sum = 0
    for i in str(z):
        sum = sum + int(i)
    # print(sum)
    if isPrime(sum):
        print("YES")
    else:
        print("NO")
