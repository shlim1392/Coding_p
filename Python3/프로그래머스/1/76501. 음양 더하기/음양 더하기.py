def solution(a, s):
    res = [num if cond else -num for cond, num in zip(s, a)]
    return sum(res)