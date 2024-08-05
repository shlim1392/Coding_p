def solution():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    array = list(map(int, data[2:N+2]))
    
    queries = []
    for i in range(M):
        queries.append((int(data[N+2 + 2*i]), int(data[N+2 + 2*i + 1])))
    
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + array[i - 1]
    
    results = []
    for i, j in queries:
        results.append(prefix_sum[j] - prefix_sum[i - 1])
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")

solution()
