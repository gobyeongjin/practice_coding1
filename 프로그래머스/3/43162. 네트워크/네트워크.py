def dfs(computers, visited, i, n):
    visited[i] = True
    for j in range(n):
        if computers[i][j] == 1 and not visited[j]:
            dfs(computers, visited, j, n)

def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        if not visited[i]: 
            dfs(computers, visited, i, n) 
            answer += 1  
    
    return answer
