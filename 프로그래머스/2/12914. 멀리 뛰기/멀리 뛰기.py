def solution(n):
    answer = 0
    
    dp = [0] *(n+1)
    
    if n<3:
        return n
    
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[i] % 1234567