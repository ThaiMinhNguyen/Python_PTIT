prime = [True] * 10001
prime[0] = prime[1] = False
for i in range(2, 10001):
    if prime[i]:
        for j in range(i*i, 10001, i):
            prime[j] = False
ans = []
input()
a = list(map(int, input().split()))
for i in a:
    buoc = 0
    a1 = a2 = i
    while not prime[a1] and not prime[a2]:
        a1-=1
        a2+=1
        buoc+=1
    ans.append(buoc)
print(max(ans))

# 8
# 13 5 8 7 9 15 26 34