import math

def comb(n, m):
    return math.comb(m, n)


T = int(input())
results = []

for _ in range(T):
    N, M = map(int, input().split())
    results.append(comb(N, M))


for result in results:
    print(result)
