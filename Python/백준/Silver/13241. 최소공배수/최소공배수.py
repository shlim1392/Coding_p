import math
def solution(a,b) : 
    return abs(a*b) // math.gcd(a, b)

a, b = map(int, input().split())
print(solution(a,b))