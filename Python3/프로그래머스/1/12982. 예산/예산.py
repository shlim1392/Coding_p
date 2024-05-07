def solution(d, budget):
    d.sort()
    res = 0 
    for x in d:
        if budget >= x :
            budget -= x
            res += 1
    return res   