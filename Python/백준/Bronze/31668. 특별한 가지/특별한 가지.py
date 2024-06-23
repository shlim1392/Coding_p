n = int(input())
m = int(input())
k = int(input())

def solution(n, m, k):
    g = m // n
    res = k * g
    return res

print(solution(n,m,k))