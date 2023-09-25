n = int(input())
a = list(map(float, input().split()))
mn = min(a)
mx = max(a)
# sum = 0
# so = 0
# print(mn, mx)
# for i in a:
#     if i != mn and i != mx:
#         sum += i
#         so += 1
# # print(sum, so)
# print("{:.2f}".format((sum/so)))
a = [x for x in a if x != mn and x != mx]
print("{:.2f}".format(sum(a)/len(a)))
