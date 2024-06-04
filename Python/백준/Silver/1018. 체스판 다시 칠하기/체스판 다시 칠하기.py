N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

pattern1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
pattern2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

min_repaints = float('inf')

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        repaints1 = 0
        repaints2 = 0
        for x in range(8):
            for y in range(8):
                if board[i + x][j + y] != pattern1[x][y]:
                    repaints1 += 1
                if board[i + x][j + y] != pattern2[x][y]:
                    repaints2 += 1
        min_repaints = min(min_repaints, repaints1, repaints2)

print(min_repaints)