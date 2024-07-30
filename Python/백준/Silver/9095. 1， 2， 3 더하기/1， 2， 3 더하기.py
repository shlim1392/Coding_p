def precompute_ways():
    max_n = 11
    dp = [0] * (max_n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for i in range(4, max_n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp

dp = precompute_ways()

T = int(input().strip())
test_cases = [int(input().strip()) for _ in range(T)]

for n in test_cases:
    print(dp[n])
