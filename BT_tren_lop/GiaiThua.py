def tinh(n):
    sum = 1
    if int(n) == 0 or int(n) == 1: return n
    for i in range(1, n+1):
        sum = sum*i
    return sum

