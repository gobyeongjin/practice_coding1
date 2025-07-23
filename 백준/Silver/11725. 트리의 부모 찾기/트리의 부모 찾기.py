import sys
sys.setrecursionlimit(10**6)  

N = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
answer = [0] * (N + 1)

def dfs(st):
    visited[st] = True
    for neighbor in graph[st]:
        if not visited[neighbor]:
            answer[neighbor] = st
            dfs(neighbor)

dfs(1)


for i in range(2, N + 1):
    print(answer[i])
