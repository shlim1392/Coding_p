import math
def solution(n):
    sqrt = math.sqrt(n)
    if sqrt == int(sqrt):
        return (sqrt + 1) ** 2
    else :
        return -1