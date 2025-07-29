test_case = int(input())

for i in range(test_case):

    n = int(input())
    dp = [0] * 100

    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    
    for j in range(3,n):
        dp[j] = dp[j-3] + dp[j-2]
    

    print(dp[n-1])