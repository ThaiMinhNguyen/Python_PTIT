from collections import deque

for t in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    ans_left = [-1]
    l = deque()
    l.append(0)
    i = 1
    while i < n:
        while(len(l) != 0 and ls[l[-1]] <= ls[i]):
            l.pop()
        if len(l) != 0:
            ans_left.append(l[-1])
        else:
            ans_left.append(-1)
        l.append(i)
        i+=1

    ans_right = [-1]
    r = deque()
    r.append(n-1)
    j = n - 2
    while j >= 0:
        while len(r) != 0 and ls[r[-1]] > ls[j]:
            r.pop()
        if len(r) != 0:
            ans_right.insert(0, r[-1])
        else:
            ans_right.insert(0, -1)
        r.append(j)
        j-=1
    cnt = 0
    for i in range(n):
        if(ans_left[i] == ans_right[i] == -1):
            cnt+=1
    print(cnt)

