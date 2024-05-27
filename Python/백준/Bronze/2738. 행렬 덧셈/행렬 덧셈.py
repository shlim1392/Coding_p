N, M = map(int, input().split()) 

matrix1 = [list(map(int, input().split())) for _ in range(N)]
matrix2 = [list(map(int, input().split())) for _ in range(N)]

result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(M)] for i in range(N)]

for row in result_matrix:
    print(*row)

        