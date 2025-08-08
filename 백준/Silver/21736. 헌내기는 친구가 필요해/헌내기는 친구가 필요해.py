from collections import deque

N , M = map(int,input().split())
school = [ list(input()) for i in range(N)]


visited = [M*[False] for _ in range(N)]

def bfs (x,y):
    visited[x][y] = True
    count = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    que = deque([(x,y)])

    while que:
        i,j = que.popleft()
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and school[nx][ny] != 'X':
                    visited[nx][ny] = True
                    que.append((nx, ny))
                    if school[nx][ny] == 'P':
                        count += 1
    
    return count



for i in range(N):
    for j in range(M):
        if school[i][j] == 'I':
            result = bfs(i,j)

print(result if result > 0 else 'TT')


