from sys import setrecursionlimit

setrecursionlimit(10**6)

n = int(input())
color = [0] * (n*3)
dothi = dict()
ke = [[] for _ in range(n*3)]
idx = 1
def DFS(u):
    color[u] = 1
    for v in ke[u]:
        if not color[v]:
            if DFS(v): return True
        elif color[v] == 1:
            return True
    color[u] = 2
    return False

def solve():
    for i in range(idx):
        if not color[i]:
            if DFS(i):
                return "impossible"
    return "possible"

for _ in range(n):
    name1, s, name2 = input().split()
    # print(name1, name2)
    if name1 not in dothi:
        dothi[name1] = idx
        idx+=1
    if name2 not in dothi:
        dothi[name2] = idx
        idx+=1
    # print(dothi)
    if s == ">":
        ke[dothi[name1]].append(dothi[name2])
    else:
        ke[dothi[name2]].append(dothi[name1])
print(solve())
# 3
# An > Binh
# Binh > Cong
# An < Cong