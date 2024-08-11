import sys
input = sys.stdin.read

data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))

M = int(data[N+1])
queries = list(map(int, data[N+2:]))

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

result = []
for k in range(M):
    i = queries[2 * k]
    j = queries[2 * k + 1]
    result.append(prefix_sum[j] - prefix_sum[i - 1])

print("\n".join(map(str, result)))
