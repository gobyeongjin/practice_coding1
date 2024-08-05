from collections import deque

def bfs():
    lst1 = [row[:] for row in lst]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque()
    set1 = set()

    for i in range(n):
        for j in range(m):
            if lst1[i][j] == 2:
                q.append((i, j))
                set1.add((i, j))

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and lst1[nx][ny] == 0 and (nx, ny) not in set1:
                lst1[nx][ny] = 2
                set1.add((nx, ny))
                q.append((nx, ny))

    global answer
    cnt=0

    for i in range(n):
        cnt+= lst1[i].count(0)

    answer =  max(answer,cnt)

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if lst[i][j]==0:
                lst[i][j] = 1
                makeWall(cnt+1)
                lst[i][j] = 0





n,m= map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(n)]

answer = 0
makeWall(0)
print(answer)