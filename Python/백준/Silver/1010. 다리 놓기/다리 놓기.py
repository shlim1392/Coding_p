import math

def combination(n, m):
    return math.comb(m, n)

T = int(input())
results = []

for _ in range(T):
    N, M = map(int, input().split())
    results.append(combination(N, M))

for result in results:
    print(result)
