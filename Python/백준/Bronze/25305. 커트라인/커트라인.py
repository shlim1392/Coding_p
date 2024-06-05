def solution(k, x):
    a = sorted(x, reverse=True)
    res = a[k-1]
    return res

n, k = map(int, input().split())
x = list(map(int, input().split()))

print(solution(k, x))