def solution(a, b):
    res = 0
    for x in range(len(a)):
        res +=a[x] * b[x]
    return res