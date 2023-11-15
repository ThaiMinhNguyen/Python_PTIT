
import math
def Try(n, k):
    s = math.pow(2, n-1)
    if(k == s):
        return chr(ord('A') + n - 1)
    if(k < s):
        return Try(n-1, k)
    else :
        return Try(n-1, k-s)




for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    print(Try(n, k))
