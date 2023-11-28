def solution(a, b):
    x = int(str(a) + str(b))
    y = 2*a*b
    return x if x == y else max(x,y)