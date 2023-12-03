
def DFS(u, visited):
    global res
    visited[u] = True
    for i in canh[u]:
        if not visited[i]:
            visited[i] = True
            res.append(i)
            DFS(i, visited)

n, m, v = map(int, input().split())
n += 1
visited = [False] * n
canh = [[] for i in range(n+1)]
res = []
# visited[v] = True
for _ in range(m):
    a, b = map(int, input().split())
    canh[a].append(b)
    canh[b].append(a)

# for i in range(1, n+1):
#     DFS(i, v, visited)
DFS(v, visited)
# print(*res)
for i in range(1, n):
    if i not in res and i != v:
        print(i)


# 6 4 2
# 1 3
# 2 3
# 1 2
# 4 5