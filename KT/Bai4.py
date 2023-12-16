def DFS(u, visited):
    global res
    visited[u] = True
    for i in canh[u]:
        if not visited[i]:
            visited[i] = True
            # res.append(i)
            DFS(i, visited)

for _ in range(int(input())):
    n, m = map(int, input().split())
    n += 1
    # visited = [False] * n
    canh = [[] for i in range(n + 1)]
    # res = []
    for i in range(m):
        a, b = map(int, input().split())
        canh[a].append(b)
        canh[b].append(a)
    res = 0
    mx = 0
    for i in range(1, n):
        cnt = 0
        visited = [False] * n
        visited[i] = True
        for j in range(1, n):
            if not visited[j]:
                DFS(j, visited)
                cnt += 1
        # print(cnt)
        if cnt > mx:
            mx = cnt
            res = i
    if mx > 1:
      print(res)
    else:
        print(0)


# 2
# 5 5
# 1 2
# 1 3
# 2 3
# 3 4
# 3 5
# 5 7
# 1 2
# 1 3
# 2 3
# 2 5
# 3 4
# 3 5
# 4 5
