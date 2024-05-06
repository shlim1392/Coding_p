from itertools import combinations
def solution(number):
    res = 0
    comb_list = combinations(number, 3)
    sum_list = [sum(comb) for comb in comb_list]
    for x in sum_list:
        if x == 0:
            res += 1        
    return res