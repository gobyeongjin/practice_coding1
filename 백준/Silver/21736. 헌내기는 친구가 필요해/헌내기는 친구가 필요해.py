from collections import deque

def bfs(i, j):
    q = deque([(i, j)])
    set1 = set()
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    answer = 0
    
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in set1:
                if lst[nx][ny] == "O":
                    q.append((nx, ny))
                    set1.add((nx, ny))
                elif lst[nx][ny] == "P":
                    answer += 1
                    q.append((nx, ny))
                    set1.add((nx, ny))
                    
    return answer

n, m = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if lst[i][j] == 'I':
            if bfs(i,j)==0:
                print('TT')
            else:
                print(bfs(i,j))
