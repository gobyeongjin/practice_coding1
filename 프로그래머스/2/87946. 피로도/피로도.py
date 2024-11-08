def solution(k, dungeons):
    answer = [-1]
    
    visited = [False] * len(dungeons)
    dfs(k, dungeons, visited, answer, 0)
    
    return answer[0]

def dfs(k, dungeons, visited, answer, score ):
    
    answer[0] = max(answer[0], score)
    for i in range(len(dungeons)):
        if not visited[i] and k>= dungeons[i][0]:
            visited[i] = True
            dfs(k-dungeons[i][1], dungeons, visited, answer, score+1)
            visited[i] = False