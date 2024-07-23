def solution(N):

    for i in range(1, N + 1):
        print('*' * i)
    

    for j in range(N - 1, 0, -1):
        print('*' * j)


N = int(input())
solution(N)
