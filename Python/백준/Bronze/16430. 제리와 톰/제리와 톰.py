import math

def solution(A, B):
    P = B - A
    Q = B
    
    gcd = math.gcd(P, Q)
    P //= gcd
    Q //= gcd
    
    return P, Q

A, B = map(int, input().split())
P, Q = solution(A, B)
print(P, Q)
