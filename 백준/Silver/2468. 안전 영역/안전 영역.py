from collections import deque

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

max_height = max(max(row) for row in lst)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, rain):
    queue = deque([(i, j)])
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and lst[nx][ny] > rain:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

max_safe_area = 0

for rain in range(max_height + 1):  
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and lst[i][j] > rain:
                bfs(i, j, rain )
                count += 1

    max_safe_area = max(max_safe_area, count)

print(max_safe_area)
