n = int(input())

for _ in range(n):
    v, e = map(int, input().split())
    res = 2 - v + e
    print(res)