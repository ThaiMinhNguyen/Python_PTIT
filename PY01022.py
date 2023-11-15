def sumOfDigits(n):
    sum = 0
    for i in n:
        sum += ord(i) - ord('0')
    return sum

x = input()
res = 1
x = str(sumOfDigits(x))
while(len(x) > 1):
    x = str(sumOfDigits(x))
    res+=1
print(res)

