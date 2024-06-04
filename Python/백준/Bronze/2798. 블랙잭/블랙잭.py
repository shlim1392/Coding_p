import itertools as it

def solution(m, num):
    res = []
    comb = it.combinations(num, 3)  
    for c in comb:
        if sum(c) <= m: 
            res.append(sum(c))
    return max(res) 

n, m = map(int, input().split())
num = list(map(int, input().split()))

print(solution(m, num))