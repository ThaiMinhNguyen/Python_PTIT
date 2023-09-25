for t in range(int(input())):
    m = 0
    ans = 10000001
    n = int(input())
    a = list(map(int, input().split()))
    myMap = {}
    for i in a:
        if i not in myMap:
            myMap[i] = 1
        else:
            myMap[i] += 1
    m = max(myMap.values())
    if(m > n/2):
        for k, v in myMap.items():
            if(m == v):
              ans = min(ans,k)
        print(ans)
    else:
        print("NO")


