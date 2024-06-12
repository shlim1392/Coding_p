import math

def solution(n):
    lcm = n * 6 // math.gcd(n, 6)
    res = lcm // 6
    return res