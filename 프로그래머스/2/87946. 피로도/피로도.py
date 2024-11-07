def solution(k, dungeons):
    answer = [0] 
    visited = [False for _ in range(len(dungeons))]
    dfs(k, 0, dungeons, visited, answer)
    return answer[0]

def dfs(k, cnt, dungeons, visited, answer):
    if cnt > answer[0]:
        answer[0] = cnt
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited, answer)
            visited[i] = False
