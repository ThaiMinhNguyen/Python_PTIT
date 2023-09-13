for t in range(int(input())):
    x = int(input())
    sum = 0;
    if x % 2 == 0:
        for i in range(2, x+1, 2):
            sum += 1/i
    else:
        for i in range(1, x + 1, 2):
            sum += 1/i
    print("{:.6f}".format(sum))