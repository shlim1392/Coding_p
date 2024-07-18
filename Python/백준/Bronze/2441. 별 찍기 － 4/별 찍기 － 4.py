def solution(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)

n = int(input())
solution(n)
