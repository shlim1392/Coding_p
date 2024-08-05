def solution():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    triangle = []
    index = 1
    
    for i in range(1, n + 1):
        triangle.append(list(map(int, data[index:index + i])))
        index += i


    dp = [[0] * (i + 1) for i in range(n)]
    dp[0][0] = triangle[0][0]


    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]


    print(max(dp[-1]))

solution()
