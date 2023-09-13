


n = int(input())
x = []

# for i in range (0, n):
#     k = int(input())
#     x.append(k)

x = list(map(int, input().split()))

check = 0
print(len(x))



# for i in range(0,len(x)-1):
#     if(x[i] % 2 == 0):
#         x.pop(i)

for i in  range(0,len(x)):
    print(x[i])


# while(check == 0):
#     check = 1
#     for i in (0,len(x)-1):
#         if x[i] % 2 == 0:
#             x.pop(i)
#             x.pop(i+1)
#             check = 0
#             n = n-2
#             break

print(x)