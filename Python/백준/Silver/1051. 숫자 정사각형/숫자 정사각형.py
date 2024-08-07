def largest_square(N, M, grid):
    max_size = 0
    
    for i in range(N):
        for j in range(M):

            for k in range(min(N - i, M - j)):
                if grid[i][j] == grid[i + k][j] == grid[i][j + k] == grid[i + k][j + k]:
                    max_size = max(max_size, (k + 1) ** 2)
    
    return max_size


N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

print(largest_square(N, M, grid))
