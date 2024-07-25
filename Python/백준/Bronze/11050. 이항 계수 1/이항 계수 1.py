def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def solution(N, K):
    return factorial(N) // (factorial(K) * factorial(N - K))


N, K = map(int, input().strip().split())

print(solution(N, K))
