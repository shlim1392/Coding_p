def solution():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    B = list(map(int, data[N+1:2*N+1]))
    
    A.sort(reverse=True)
    B.sort()

    S = sum(A[i] * B[i] for i in range(N))
    
    print(S)

solution()
