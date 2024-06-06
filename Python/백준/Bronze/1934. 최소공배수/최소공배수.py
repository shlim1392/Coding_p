import math

def solution(a, b):
    return abs(a*b) // math.gcd(a,b)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(solution(a,b))

