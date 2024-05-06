from itertools import combinations
def solution(numbers):
    comb = combinations(numbers, 2)
    res = [ x * y for x,y in comb]
    return max(res)