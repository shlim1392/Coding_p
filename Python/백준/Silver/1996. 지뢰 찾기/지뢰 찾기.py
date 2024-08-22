def solution():
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]
    result = [[0] * N for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] != '.':
                mine_count = int(grid[i][j])
                result[i][j] = '*'  
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == '.':
                        result[ni][nj] += mine_count
    
    for i in range(N):
        for j in range(N):
            if result[i][j] != '*':
                if result[i][j] >= 10:
                    result[i][j] = 'M'
                else:
                    result[i][j] = str(result[i][j])
    
    for row in result:
        print("".join(row))

solution()