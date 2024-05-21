import itertools
def solution(numbers):
    a = []
    combi = list(itertools.combinations(numbers, 2))
    for com in combi:
        b = com[0] * com[1]
        a.append(b)
    return max(a)