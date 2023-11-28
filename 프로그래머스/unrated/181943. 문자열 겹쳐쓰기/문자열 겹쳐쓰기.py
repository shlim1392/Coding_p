def solution(a, b, s):
    return a[:s] + b + a[s+len(b):]