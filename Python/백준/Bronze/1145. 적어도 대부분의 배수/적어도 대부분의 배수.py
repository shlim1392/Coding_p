import math
from itertools import combinations

def lcm(a, b):
    return a * b // math.gcd(a, b)

def lcm_of_three(a, b, c):
    return lcm(lcm(a, b), c)

def solution():
    nums = list(map(int, input().split()))
    min_lcm = float('inf')
    
    for comb in combinations(nums, 3):
        a, b, c = comb
        current_lcm = lcm_of_three(a, b, c)
        if current_lcm < min_lcm:
            min_lcm = current_lcm
    
    print(min_lcm)

solution()
