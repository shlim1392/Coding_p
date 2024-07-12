def count_diagonal_neighbors(N, M):
    count = 0
    for i in range(N - 1):
        for j in range(M - 1):
            count += 1
    
    for i in range(N - 1):
        for j in range(1, M):
            count += 1
    
    return count


N = int(input().strip())
M = int(input().strip())

print(count_diagonal_neighbors(N, M))
