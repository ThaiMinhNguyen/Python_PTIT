a = input()
k = 0
for i in range(len(a)):
    if(a[i] == '4' or a[i] == '7'):
        k = k+1
if(k == 4 or k == 7):
    print("YES")
else:
    print("NO")