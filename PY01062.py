import math
def isPrime(n):
    for i in range(2, int(math.sqrt(int(n)))+1):
        if n % i == 0:
            return False
    return n > 1

for t in range(int(input())):
    s = input()
    sum = 0
    for i in s :
        if(isPrime(int(i))):
            sum = sum + 1;
    if(isPrime(len(s)) and sum > len(s) - sum) :
        print("YES")
    else:
        print("NO")