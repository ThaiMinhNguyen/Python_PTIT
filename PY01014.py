a, k, n = map(int, input().split())
b = k - (a%k)
check = 0
for i in range(b, n-a+1, k):
    if (a + i) % k == 0:
        check = 1
        print(i, end = " ")
if(check == 0):
    print(-1)