def DFS(u, visited):
    global res
    visited[u] = True
    for i in canh[u]:
        if not visited[i]:
            visited[i] = True
            res.append(i)
            DFS(i, visited)

n, m = int(input()), int(input())
n+=1
visited = [False] * n
canh = [[] for i in range(n+1)]
res = []
for _ in range(m):
    a, b = map(int, input().split())
    canh[a].append(b)
    canh[b].append(a)

def solve():
    for i in range(1, n):
        if not visited[i]:
            res.clear()
            DFS(i, visited)
            if len(res) > 1:
                for j in res:
                    if len(canh[j]) != len(res):
                        return "NO"
    return "YES"

print(solve())