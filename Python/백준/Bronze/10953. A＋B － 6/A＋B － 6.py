def solution(n):
    for _ in range(n):
        a, b = map(int, input().split(","))
        print(a + b)


n = int(input())
solution(n)
