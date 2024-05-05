def solution(s):
    return isinstance(s, str) and s.isdigit() and (len(s) == 4 or len(s) == 6)