from collections import deque

# BFS를 사용하여 석유 덩어리의 크기를 계산하는 함수
def bfs(x, y, land, n, m, visited, oil_id):
    q = deque()
    q.append((x, y))
    visited[x][y] = oil_id
    area_size = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and land[nx][ny] == 1:
                visited[nx][ny] = oil_id
                q.append((nx, ny))
                area_size += 1
                
    return area_size

def solution(land):
    n = len(land)
    m = len(land[0])
    
    visited = [[0] * m for _ in range(n)]
    oil_id = 1
    oil_sizes = {}
    
    # 석유 덩어리의 크기를 계산하여 저장
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                size = bfs(i, j, land, n, m, visited, oil_id)
                oil_sizes[oil_id] = size
                oil_id += 1
    
    max_oil = 0
    
    # 각 열에 대해 석유량을 계산
    for j in range(m):
        column_oil = set()  # 이 열을 지나는 석유 덩어리 ID를 저장
        total_oil = 0
        for i in range(n):
            if visited[i][j] != 0:
                oil_id = visited[i][j]
                if oil_id not in column_oil:
                    column_oil.add(oil_id)
                    total_oil += oil_sizes[oil_id]
        max_oil = max(max_oil, total_oil)
    
    return max_oil
