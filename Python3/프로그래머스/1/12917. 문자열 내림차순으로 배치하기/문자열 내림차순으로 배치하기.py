def solution(s):
    res = sorted(list(s), reverse=True)
    return ''.join(res)