from collections import deque

M, N, K = map(int, input().split())


lst = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):    
        for j in range(x1, x2):  
            lst[i][j] = 1


visited= [[False]* N for _ in range(M)]

def bfs(x,y):
    queue = deque([(x, y)])

    visited[x][y] = True
    area = 1

    dx=[1,-1,0,0]
    dy=[0,0,-1,1]

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny] and lst[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    area += 1
    return area

result = []

for i in range(M):
    for j in range(N):
        if not visited[i][j] and lst[i][j] == 0:
            result.append(bfs(i,j))

result.sort()
print(len(result))

print(' '.join(map(str, result)))
