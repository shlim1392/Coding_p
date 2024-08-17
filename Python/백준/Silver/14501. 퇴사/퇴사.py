def max_profit(n, schedules):
    dp = [0] * (n + 2)
    
    for i in range(n, 0, -1):
        t, p = schedules[i-1]
        if i + t <= n + 1:
            dp[i] = max(dp[i + t] + p, dp[i + 1])
        else:
            dp[i] = dp[i + 1]
    
    return dp[1]

n = int(input())
schedules = []
for _ in range(n):
    t, p = map(int, input().split())
    schedules.append((t, p))

print(max_profit(n, schedules))
