import math

def solution(n):
    sqrt_n = math.isqrt(n)
    if sqrt_n * sqrt_n == n:
        return 1
    else:
        return 2