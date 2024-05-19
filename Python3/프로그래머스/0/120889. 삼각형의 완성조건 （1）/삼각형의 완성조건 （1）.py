
def solution(sides):
    a = max(sides)     
    return 1 if a < (sum(sides) - a) else 2