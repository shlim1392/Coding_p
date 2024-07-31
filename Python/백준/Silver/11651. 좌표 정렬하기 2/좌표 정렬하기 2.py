def solution(n):
    res = []
    for _ in range(n):
        a = list(map(int, input().split()))
        res.append(a)
    res.sort(key=lambda x: (x[1], x[0]))
    for pair in res:
        print(" ".join(map(str, pair)))

n = int(input())
solution(n)