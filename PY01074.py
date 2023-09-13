import math
# sum = 0
# for t in range(int(input())):
#     x = int(input())
#     i = 2
#     while(x > 1):
#         while(x % i == 0):
#             sum = sum + i
#             x = x/i
#         i = i+1
#     if x > 1:
#         sum = sum + x
# print(int(sum))

sum = 0
a = [0] * 2000005
for i in range(2, int(math.sqrt(2000000))+1):
    if a[i] == 0:
        for j in range(i*i, 2000001, i):
            if a[j] == 0:
                a[j] = int(i)
for i in range(2, 2000001):
    if a[i] == 0 :
        a[i] = i
for t in range(int(input())):
    x = int(input())
    while(x > 1):
        sum = sum + a[x]
        x = int(x / a[x])
print(sum)

